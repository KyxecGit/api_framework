from typing import List
from pydantic import BaseModel


class GenreResponse(BaseModel):
    """Модель для представления информации о жанре."""
    
    id: int  # Уникальный идентификатор жанра
    name: str  # Название жанра


class GenreListResponse(BaseModel):
    """Модель для представления списка жанров."""
    
    genres: List[GenreResponse]  # Список жанров
