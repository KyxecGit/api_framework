from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict

from services.payment.models.status_enumerate import Status


class PaymentResponse(BaseModel):
    """Модель для ответа о платеже."""

    model_config = ConfigDict(populate_by_name=True)

    id: int
    total: int
    amount: int
    status: Status
    user_id: UUID = Field(alias="userId")
    movie_id: int = Field(alias="movieId")
    created_at: str = Field(alias="createdAt")
