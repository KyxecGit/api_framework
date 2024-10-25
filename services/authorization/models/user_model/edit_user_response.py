import datetime
from typing import List
from pydantic import BaseModel, Field, ConfigDict

from services.authorization.models.roles_enumerate import RolesEnumeration


class EditUserResponse(BaseModel):
    """Модель для представления ответа на запрос редактирования пользователя."""

    model_config = ConfigDict(populate_by_name=True)  # Конфигурация модели для заполнения по именам

    email: str  # Электронная почта пользователя
    verified: bool  # Статус верификации пользователя
    banned: bool  # Статус бана пользователя
    roles: List[RolesEnumeration]  # Список ролей пользователя
    created_at: datetime.datetime = Field(alias="createdAt", default=None)  # Дата создания пользователя
    full_name: str = Field(alias="fullName")  # Полное имя пользователя
