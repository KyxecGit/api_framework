from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from typing import List, Optional
import datetime

from services.authorization.models.roles_enumerate import RolesEnumeration


class UserResponse(BaseModel):
    """Модель для представления ответа на запрос пользователя."""

    model_config = ConfigDict(populate_by_name=True)  # Конфигурация модели для заполнения по именам

    id: UUID  # Уникальный идентификатор пользователя
    email: str  # Электронная почта пользователя
    banned: Optional[bool] = None  # Статус бана пользователя (опционально)
    roles: List[RolesEnumeration]  # Список ролей пользователя
    verified: Optional[bool] = None  # Статус верификации пользователя (опционально)
    created_at: Optional[datetime.datetime] = Field(alias="createdAt", default=None)  # Дата создания пользователя (опционально)
    full_name: str = Field(alias="fullName")  # Полное имя пользователя
