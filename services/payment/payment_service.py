from typing import List

from services.payment.helpers.payment_helper import PaymentHelper
from services.payment.models.create_payment import CreatePayment
from services.payment.models.payment_registrated import PaymentRegistrated
from services.payment.models.payment_response import PaymentResponse
from utils.config import UrlConfig


class PaymentService:
    def __init__(self, url: UrlConfig):
        self.url = url
        self.payment_helper = PaymentHelper(url)

    def update_api_utils_token(self, token: str):
        """Обновить заголовки API с токеном авторизации."""
        self.url.update_headers(headers={"Authorization": f"Bearer {token}"})

    def update_api_utils(self, headers: dict):
        """Обновить заголовки API с переданными заголовками."""
        self.url.update_headers(headers=headers)

    def post_create(self, create_payment_dto: CreatePayment) -> PaymentRegistrated:
        """Создать платеж и вернуть его статус."""
        response = self.payment_helper.post_create(
            json=create_payment_dto.model_dump(by_alias=True, exclude_defaults=True)
        )
        return PaymentRegistrated(**response.json())

    def get_user(self) -> List[PaymentResponse]:
        """Получить список платежей пользователя."""
        response = self.payment_helper.get_user()
        return [PaymentResponse(**payment) for payment in response.json()]

    def get_user_id(self, user_id: int) -> List[PaymentResponse]:
        """Получить платежи по идентификатору пользователя."""
        response = self.payment_helper.get_user_id(user_id=user_id)
        return [PaymentResponse(**payment) for payment in response.json()]
