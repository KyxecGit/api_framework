from pydantic import BaseModel


class CreateGenre(BaseModel):
    """Модель для создания нового жанра."""

    name: str  # Название жанра
