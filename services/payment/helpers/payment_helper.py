import requests
import json
from services.base_helper import BaseHelper


class PaymentHelper(BaseHelper):
    """Помощник для работы с платежами и пользователями."""

    PAYMENT_ENDPOINT = "create/"
    USER_ENDPOINT = "user/"

    def post_create(self, json: json) -> requests.Response:
        """Создает новый платеж."""
        response = self.url.post(self.PAYMENT_ENDPOINT, json=json)
        return response

    def get_user_id(self, user_id: int) -> requests.Response:
        """Получает информацию о пользователе по его ID."""
        response = self.url.get(self.USER_ENDPOINT + str(user_id))
        return response

    def get_user(self) -> requests.Response:
        """Получает информацию о текущем пользователе."""
        response = self.url.get(self.USER_ENDPOINT)
        return response
