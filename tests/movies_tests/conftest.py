import pytest
from faker import Faker

from services.movies.movies_service import MoviesService
from tests.conftest import email, password
from utils.config import UrlConfig
from services.authorization.auth_service import AuthService
from services.authorization.models.auth_model.login import Login
from utils.api_util import ApiUtils

# Инициализация Faker для генерации тестовых данных
faker = Faker()

# Фикстура для настройки API-утилит для работы с фильмами
@pytest.fixture(scope="session", autouse=False)
def movie_api_utilities(auth_api_utilities):
    # Создание экземпляра AuthService для аутентификации
    auth_service = AuthService(url=auth_api_utilities)
    
    # Создание DTO для логина
    login_dto = Login(email=email, password=password)
    
    # Выполнение логина и получение токена доступа
    login_response = auth_service.login_user(login_dto)

    # Настройка API-утилит с токеном доступа
    api_utils_super_admin = ApiUtils(UrlConfig.MOVIE_URL, headers={
        "Authorization": f"Bearer {login_response.access_token}"})

    # Возврат настроенных API-утилит для дальнейшего использования в тестах
    yield api_utils_super_admin


# Фикстура для настройки сервиса работы с фильмами
@pytest.fixture(scope="session", autouse=False)
def movie_api_service(movie_api_utilities):
    # Создание экземпляра MoviesService с переданными API-утилитами
    api_service = MoviesService(movie_api_utilities)
    
    # Возврат сервиса для использования в тестах
    yield api_service
