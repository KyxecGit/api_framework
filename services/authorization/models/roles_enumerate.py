from enum import Enum


class RolesEnumeration(str, Enum):
    """Перечисление ролей пользователей."""

    USER = "USER"  # Обычный пользователь
    ADMIN = "ADMIN"  # Администратор
    SUPER_ADMIN = "SUPER_ADMIN"  # Супер администратор
