from typing import List
from pydantic import BaseModel

from services.authorization.models.roles_enumerate import RolesEnumeration


class EditUser(BaseModel):
    """Модель для представления данных редактирования пользователя."""

    roles: List[RolesEnumeration]  # Список ролей пользователя
    verified: bool  # Статус верификации пользователя
    banned: bool  # Статус бана пользователя
