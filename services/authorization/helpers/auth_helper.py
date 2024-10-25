import requests
import json

from services.base_helper import BaseHelper


class AuthHelper(BaseHelper):
    """Помощник для аутентификации пользователей."""

    REGISTER_ENDPOINT = 'register/'  # Эндпоинт для регистрации пользователей
    LOGIN_ENDPOINT = 'login/'  # Эндпоинт для входа пользователей

    def post_register_user(self, json: dict) -> requests.Response:
        """Отправляет POST-запрос для регистрации нового пользователя.

        :param json: Данные пользователя в формате JSON
        :return: Ответ сервера в виде объекта Response
        """
        response = self.url.post(self.REGISTER_ENDPOINT, json=json)  # Выполняем запрос на регистрацию
        return response

    def post_login_user(self, json: dict) -> requests.Response:
        """Отправляет POST-запрос для входа пользователя.

        :param json: Данные пользователя в формате JSON
        :return: Ответ сервера в виде объекта Response
        """
        response = self.url.post(self.LOGIN_ENDPOINT, json=json)  # Выполняем запрос на вход
        return response
