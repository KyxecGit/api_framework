import requests
from services.base_helper import BaseHelper
import json


class GenreHelper(BaseHelper):
    """Помощник для работы с жанрами."""

    GENRES_ENDPOINT = "genres/"  # Эндпоинт для работы с жанрами

    def get_genres(self) -> requests.Response:
        """Получить список жанров."""
        response = self.url.get(self.GENRES_ENDPOINT)  # Выполнить GET-запрос на получение жанров
        return response  # Вернуть ответ

    def post_genre(self, json: json) -> requests.Response:
        """Добавить новый жанр."""
        response = self.url.post(self.GENRES_ENDPOINT, json=json)  # Выполнить POST-запрос для добавления жанра
        return response  # Вернуть ответ
