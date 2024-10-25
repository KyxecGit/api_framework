from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from services.movies.models.genre_model.genre import Genre
from services.movies.models.location_enumerate import LocationEnum


class MovieResponse(BaseModel):
    """Модель ответа при получении данных о фильме."""

    model_config = ConfigDict(populate_by_name=True)

    id: int  # Идентификатор фильма
    name: str  # Название фильма
    price: float  # Цена фильма
    description: str  # Описание фильма
    location: LocationEnum  # Место съемки (перечисление)
    published: bool  # Статус публикации (опубликован/не опубликован)
    genre: Genre  # Жанр фильма
    image_url: str = Field(alias="imageUrl", default=None)  # URL изображения фильма (по умолчанию None)
    created_at: datetime = Field(alias="createdAt")  # Дата создания записи о фильме
    genre_id: int = Field(alias="genreId")  # Идентификатор жанра фильма
    rating: int = Field(ge=0, le=5)  # Рейтинг фильма (от 0 до 5)
