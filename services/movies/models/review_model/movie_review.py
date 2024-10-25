from pydantic import BaseModel, Field

class MovieReview(BaseModel):
    """Модель отзыва о фильме."""

    rating: int = Field(ge=0, le=5)  # Рейтинг отзыва (от 0 до 5)
    text: str  # Текст отзыва
