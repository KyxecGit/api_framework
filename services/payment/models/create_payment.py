from pydantic import BaseModel, Field, ConfigDict

from services.payment.models.card import Card


class CreatePayment(BaseModel):
    """Модель для создания платежа."""

    model_config = ConfigDict(populate_by_name=True)

    movie_id: int = Field(alias="movieId")
    amount: int
    card: Card
