from faker import Faker
import requests
from services.movies.helpers.genre_helper import GenreHelper
from services.movies.models.genre_model.genre import Genre

# Инициализация Faker для генерации тестовых данных
faker = Faker()


class TestGenreCreateContract:
    def test_genre_create_anonym_contract(self, movie_api_utilities):
        """
        Тест на создание жанра анонимно.
        """

        # Создаем экземпляр GenreHelper для работы с жанрами
        genre_helper = GenreHelper(movie_api_utilities)

        # Генерируем случайное имя жанра
        genre = Genre(name=faker.name())

        # Отправляем запрос на создание жанра
        response = genre_helper.post_genre(genre.model_dump())

        # Получаем статус-код ответа
        actual_status_code = response.status_code

        # Ожидаемый статус-код для успешного создания жанра
        expected_status_code = requests.status_codes.codes.created

        # Проверяем, что статус-код соответствует ожидаемому
        assert actual_status_code == expected_status_code, \
            f"Expected status code: {expected_status_code}, got instead status code: {actual_status_code}"
