import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class User(BaseModel):
    """Модель пользователя, оставившего отзыв."""
    full_name: str = Field(alias="fullName")  # Полное имя пользователя


class MovieReviewResponse(BaseModel):
    """Модель ответа при получении отзыва о фильме."""

    model_config = ConfigDict(populate_by_name=True)

    created_at: datetime.datetime = Field(alias="createdAt")  # Дата создания отзыва
    user_id: str = Field(alias="userId")  # Идентификатор пользователя, оставившего отзыв
    rating: int = Field(ge=0, le=5)  # Рейтинг отзыва (от 0 до 5)
    hidden: Optional[bool] = None  # Статус скрытия отзыва (по умолчанию None)
    text: str  # Текст отзыва
    user: User  # Информация о пользователе
