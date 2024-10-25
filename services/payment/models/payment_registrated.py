from pydantic import BaseModel

from services.payment.models.status_enumerate import Status


class PaymentRegistrated(BaseModel):
    """Модель для зарегистрированного платежа."""

    status: Status
