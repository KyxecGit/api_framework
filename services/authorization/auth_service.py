from uuid import UUID
from services.authorization.helpers.auth_helper import AuthHelper
from services.authorization.helpers.user_helper import UserHelper
from services.authorization.models.user_model.edit_user_dto import EditUser
from services.authorization.models.user_model.edit_user_response import EditUserResponse
from services.authorization.models.auth_model.login import Login
from services.authorization.models.auth_model.login_response import LoginResponse
from services.authorization.models.user_model.user_response import UserResponse
from services.authorization.models.auth_model.register import Register
from utils.config import UrlConfig


class AuthService:
    """Сервис для управления аутентификацией и пользователями."""

    def __init__(self, url: UrlConfig):
        """Инициализация сервиса с URL конфигурацией."""
        self.url = url
        self.user_helper = UserHelper(url)  # Помощник для операций с пользователями
        self.authorization_helper = AuthHelper(url)  # Помощник для операций аутентификации

    def update_api_utils(self, token: str = None, headers: dict = None):
        """Обновить заголовки API с токеном аутентификации, если предоставлен."""
        if token:
            headers = headers or {}
            headers.update({"Authorization": f"Bearer {token}"})  # Добавление токена к заголовкам
        if headers:
            self.url.update_headers(headers=headers)  # Обновление заголовков в конфигурации URL

    def update_api_utils_token(self, token: str):
        """Обновить заголовки API только с токеном аутентификации."""
        self.url.update_headers(headers={"Authorization": f"Bearer {token}"})

    def login_user(self, login_dto: Login) -> LoginResponse:
        """Аутентификация пользователя и получение ответа с токеном."""
        response = self.authorization_helper.post_login_user(json=login_dto.model_dump(by_alias=True, exclude_defaults=True))
        return LoginResponse(**response.json())  # Возвращение ответа как LoginResponse

    def register_user(self, register_dto: Register) -> UserResponse:
        """Регистрация нового пользователя и получение его данных."""
        response = self.authorization_helper.post_register_user(json=register_dto.model_dump(by_alias=True, exclude_defaults=True))
        return UserResponse(**response.json())  # Возвращение ответа как UserResponse

    def delete_user(self, user_id: UUID):
        """Удаление пользователя по его идентификатору."""
        response = self.user_helper.delete_user(user_id=user_id)
        return response  # Возвращение ответа на удаление пользователя

    def patch_user(self, user_id: UUID, edit_user_dto: EditUser) -> EditUserResponse:
        """Обновление данных пользователя по его идентификатору."""
        response = self.user_helper.patch_user(user_id=user_id, json=edit_user_dto.model_dump())
        return EditUserResponse(**response.json())  # Возвращение ответа как EditUserResponse
