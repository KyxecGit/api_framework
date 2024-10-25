import requests
from services.base_helper import BaseHelper
import json


class MovieHelper(BaseHelper):
    """Помощник для работы с фильмами и жанрами."""

    MOVIES_ENDPOINT = "movies/"  # Эндпоинт для работы с фильмами
    GENRES_ENDPOINT = "genres/"  # Эндпоинт для работы с жанрами

    def get_movies(self) -> requests.Response:
        """Получить список фильмов."""
        response = self.url.get(self.MOVIES_ENDPOINT)  # Выполнить GET-запрос на получение фильмов
        return response  # Вернуть ответ

    def post_movie(self, json: json) -> requests.Response:
        """Добавить новый фильм."""
        response = self.url.post(self.MOVIES_ENDPOINT, json=json)  # Выполнить POST-запрос для добавления фильма
        return response  # Вернуть ответ
