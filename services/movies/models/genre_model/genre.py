from pydantic import BaseModel


class Genre(BaseModel):
    """Модель для представления жанра."""

    name: str  # Название жанра
