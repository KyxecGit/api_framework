import random
from utils.config import CardConfig
from utils.logger import Logger
import pytest
from faker import Faker
from services.authorization.models.auth_model.login import Login
from services.payment.models.card import Card
from services.payment.models.create_payment import CreatePayment

faker = Faker()


class TestPayment:
    PAYMENT_AMOUNT_VALUE = random.randint(1, 11)

    @pytest.mark.parametrize("payment_amount", ([PAYMENT_AMOUNT_VALUE]))
    def test_register_user_create_movie_payment_implementation(
        self, 
        payment_amount, 
        auth_api_service,
        payment_api_service,
        super_admin_payment_api_service, 
        register_user,
        create_new_movie
    ):
        """
        Тест для регистрации нового пользователя, создания фильма и осуществления платежа.
        """
        Logger.info(" !!! Step 1 - Register new user")
        registered_user_info = register_user

        password = registered_user_info.password
        email = registered_user_info.email

        Logger.info(" !!! Step 2 - Log in as new user")
        auth_api_service.update_api_utils_token(token=None)  # Сбрасываем токен
        login_dto = Login(email=email, password=password)  # Создаём объект для логина
        login_response = auth_api_service.login_user(login_dto=login_dto)  # Логинимся
        payment_api_service.update_api_utils_token(token=login_response.access_token)  # Обновляем токен для платежного сервиса

        Logger.info(f" !!! Step 3 - Create and pay for {payment_amount} movies")
        for i in range(1, payment_amount + 1):
            Logger.debug(f"Create {i} film")
            created_movie = create_new_movie()  # Создаём новый фильм

            Logger.debug(f"Pay for a {i} movie")
            card_dto = Card(
                card_number=CardConfig.CARD_NUMBER,
                card_holder=f"{faker.first_name()} {faker.last_name()}",
                expiration_date=CardConfig.DATE,
                security_code=CardConfig.CVV
            )
            create_payment_dto = CreatePayment(
                movie_id=created_movie.id,
                amount=random.randint(1, 10),
                card=card_dto
            )
            payment_api_service.post_create(create_payment_dto)  # Осуществляем платеж

        Logger.info(" !!! Step 4 - Get the payment total amount")
        total_amount_of_payments = super_admin_payment_api_service.get_user_id(login_response.user.id)  # Получаем все платежи пользователя

        # Проверяем, что общее количество платежей соответствует ожидаемому
        assert len(total_amount_of_payments) == payment_amount, \
            f"The total number of payments {total_amount_of_payments} does not match the expected {payment_amount}"
