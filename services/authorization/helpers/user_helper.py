from uuid import UUID
import requests

from services.base_helper import BaseHelper


class UserHelper(BaseHelper):
    """Помощник для работы с пользователями."""

    USER_ENDPOINT = "user/"  # Эндпоинт для управления пользователями

    def get_user(self) -> requests.Response:
        """Получает информацию о пользователе.

        :return: Ответ сервера в виде объекта Response
        """
        response = self.url.get(self.USER_ENDPOINT)  # Выполняем запрос для получения данных пользователя
        return response

    def delete_user(self, user_id: UUID) -> requests.Response:
        """Удаляет пользователя по указанному идентификатору.

        :param user_id: Уникальный идентификатор пользователя
        :return: Ответ сервера в виде объекта Response
        """
        response = self.url.delete(self.USER_ENDPOINT + str(user_id))  # Выполняем запрос на удаление пользователя
        return response

    def patch_user(self, user_id: UUID, json: dict) -> requests.Response:
        """Обновляет информацию о пользователе.

        :param user_id: Уникальный идентификатор пользователя
        :param json: Данные для обновления в формате JSON
        :return: Ответ сервера в виде объекта Response
        """
        response = self.url.patch(self.USER_ENDPOINT + str(user_id), json=json)  # Выполняем запрос на обновление пользователя
        return response
