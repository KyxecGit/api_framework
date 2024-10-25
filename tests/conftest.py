import os
import random
import pytest
from services.authorization.auth_service import AuthService
from services.authorization.models.auth_model.login import Login
from services.authorization.models.auth_model.register import Register
from services.movies.models.movie_model.create_movie import CreateMovie
from utils.api_util import ApiUtils
from utils.config import UrlConfig
from faker import Faker
from collections import namedtuple
from services.movies.models.location_enumerate import LocationEnum

# Задаем тестовые данные для регистрации
email =  os.environ["USER_EMAIL"]
password = os.environ["USER_PASSWORD"]
faker = Faker()

@pytest.fixture(scope="session", autouse=False)
def auth_api_utilities():
    """Фикстура для анонимных API утилит авторизации."""
    anonymous_api_utils = ApiUtils(UrlConfig.AUTH_URL)
    yield anonymous_api_utils


@pytest.fixture(scope="session", autouse=False)
def super_admin_auth_api_utilities(auth_api_utilities):
    """Фикстура для авторизации супер администратора."""
    auth_service = AuthService(url=auth_api_utilities)
    login_dto = Login(email=email, password=password)
    login_response = auth_service.login_user(login_dto)

    api_utils_super_admin = ApiUtils(UrlConfig.AUTH_URL, headers={
        "Authorization": f"Bearer {login_response.access_token}"
    })

    yield api_utils_super_admin


@pytest.fixture(scope="session", autouse=False)
def auth_api_service(super_admin_auth_api_utilities):
    """Фикстура для API сервиса авторизации."""
    api_service = AuthService(super_admin_auth_api_utilities)
    yield api_service


@pytest.fixture(scope="function")
def register_user(auth_api_service):
    """Фикстура для регистрации нового пользователя."""
    auth_api_service.update_api_utils(token=None)  # Обнуляем токен
    RegisteredUser = namedtuple('RegisteredUser', ['user', 'password', 'email'])
    
    user_email = faker.email()  # Генерируем email
    user_password = faker.password(length=8, special_chars=False)  # Генерируем пароль
    
    # Создаем DTO для регистрации
    register_dto = Register(
        email=user_email,
        full_name=f"{faker.first_name()} {faker.last_name()}",
        password=user_password,
        password_repeat=user_password
    )
    
    registered_user = auth_api_service.register_user(register_dto=register_dto)  # Регистрируем пользователя
    yield RegisteredUser(user=registered_user, password=user_password, email=user_email)  # Возвращаем данные о пользователе


@pytest.fixture(scope="function")
def create_new_movie(movie_api_service):
    """Фикстура для создания нового фильма."""
    def _create_movie(genre_id=None):
        """Вспомогательная функция для создания фильма с опциональным жанром."""
        if genre_id is not None:
            # Если передан ID жанра, создаем фильм с ним
            movie = CreateMovie(
                name=faker.name(),
                price=random.randint(500, 1000),
                description=faker.pystr(),
                location=random.choice(list(LocationEnum)),
                published=True,
                genre_id=genre_id,
                image_url=faker.url()
            )
        else:
            # Если жанр не передан, выбираем случайный жанр
            genres = movie_api_service.get_genres()
            selected_genre = random.choice(genres.genres)

            movie = CreateMovie(
                name=faker.name(),
                price=random.randint(500, 1000),
                description=faker.pystr(),
                location=random.choice(list(LocationEnum)),
                published=True,
                genre_id=selected_genre.id,
                image_url=faker.url()
            )

        created_movie = movie_api_service.post_movie(movie)  # Создаем фильм через API
        return created_movie

    return _create_movie  # Возвращаем функцию создания фильма
