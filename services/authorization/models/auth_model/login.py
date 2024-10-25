from pydantic import BaseModel


class Login(BaseModel):
    """Модель для представления данных входа пользователя."""

    email: str  # Электронная почта пользователя
    password: str  # Пароль пользователя
