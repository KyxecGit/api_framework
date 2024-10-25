import requests
from services.base_helper import BaseHelper


class ReviewHelper(BaseHelper):
    """Помощник для работы с отзывами на фильмы."""

    MOVIES_ENDPOINT = "movies/"  # Эндпоинт для работы с фильмами
    REVIEWS_ENDPOINT = "/reviews/"  # Эндпоинт для работы с отзывами
    SHOW_REVIEW_ENDPOINT = "show/"  # Эндпоинт для отображения отзывов

    def post_movie_review(self, movie_id: int, json) -> requests.Response:
        """Добавить отзыв к фильму."""
        response = self.url.post(self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT, json=json)
        return response  # Вернуть ответ

    def patch_movie_review(self, movie_id: int, user_id: str) -> requests.Response:
        """Обновить отзыв к фильму по ID пользователя."""
        response = self.url.patch(
            self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT + self.SHOW_REVIEW_ENDPOINT + user_id)
        return response  # Вернуть ответ

    def delete_review(self, movie_id: int) -> requests.Response:
        """Удалить отзыв к фильму."""
        response = self.url.delete(self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT)
        return response  # Вернуть ответ
