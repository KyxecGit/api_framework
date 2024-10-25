from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

from services.authorization.models.user_model.user_response import UserResponse


class LoginResponse(BaseModel):
    """Модель для представления ответа на запрос входа пользователя."""

    model_config = ConfigDict(populate_by_name=True)  # Конфигурация модели для заполнения по именам

    user: UserResponse  # Информация о пользователе
    access_token: str = Field(alias="accessToken")  # Токен доступа с алиасом для корректного преобразования
    refresh_token: Optional[str] = None  # Токен обновления (опционально)
    expires_in: int = Field(alias="expiresIn")  # Время жизни токена с алиасом для корректного преобразования
