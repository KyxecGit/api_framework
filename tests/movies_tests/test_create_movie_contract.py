import random
import requests.status_codes
from faker import Faker
from services.movies.helpers.movies_helper import MovieHelper
from services.movies.models.location_enumerate import LocationEnum

# Инициализация Faker для генерации тестовых данных
faker = Faker()


class TestCreateMovieContract:
    def test_create_movie_admin_contract(self, movie_api_utilities):
        """
        Тест на создание фильма администратором.
        """

        # Создаем экземпляр MovieHelper для работы с фильмами
        movie_helper = MovieHelper(movie_api_utilities)

        # Генерируем данные для нового фильма
        movie_data = {
            "name": faker.name(),  # Случайное название фильма
            "imageUrl": faker.url(),  # Случайный URL для изображения
            "price": random.randint(100, 1000),  # Случайная цена
            "description": faker.pystr(),  # Случайное описание
            "location": random.choice(list(LocationEnum)),  # Случайная локация из перечисления
            "published": True,  # Фильм опубликован
            "genreId": random.randint(2, 6)  # Случайный ID жанра
        }

        # Отправляем запрос на создание фильма
        created_movie = movie_helper.post_movie(json=movie_data)

        # Получаем статус-код ответа
        actual_status_code = created_movie.status_code

        # Ожидаемый статус-код для успешного создания фильма
        expected_status_code = requests.status_codes.codes.created

        # Проверяем, что статус-код соответствует ожидаемому
        assert actual_status_code == expected_status_code, \
            f"Expected status code: {expected_status_code}, got instead status code: {actual_status_code}"
