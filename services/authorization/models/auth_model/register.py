from pydantic import BaseModel, Field, ConfigDict


class Register(BaseModel):
    """Модель для представления данных регистрации пользователя."""

    model_config = ConfigDict(populate_by_name=True)  # Конфигурация модели для заполнения по именам

    email: str  # Электронная почта пользователя
    password: str  # Пароль пользователя
    full_name: str = Field(alias="fullName")  # Полное имя пользователя с алиасом
    password_repeat: str = Field(alias="passwordRepeat")  # Повтор пароля с алиасом
