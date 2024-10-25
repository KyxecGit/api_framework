from pydantic import BaseModel, Field, ConfigDict
from services.movies.models.location_enumerate import LocationEnum


class CreateMovie(BaseModel):
    """Модель для создания нового фильма."""

    model_config = ConfigDict(populate_by_name=True)

    name: str  # Название фильма
    price: int  # Цена фильма
    description: str  # Описание фильма
    location: LocationEnum  # Место съемки (перечисление)
    published: bool  # Статус публикации (опубликован/не опубликован)
    genre_id: int = Field(alias="genreId")  # Идентификатор жанра фильма
    image_url: str = Field(alias="imageUrl", default=None)  # URL изображения фильма (по умолчанию None)
