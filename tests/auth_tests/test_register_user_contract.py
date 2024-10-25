from faker import Faker
from services.authorization.helpers.auth_helper import AuthHelper
from services.authorization.models.auth_model.login import Login
from services.authorization.models.auth_model.register import Register

# Инициализация Faker для генерации тестовых данных
faker = Faker()

class TestRegisterUser:
    def test_register_user_anonym_contract(self, auth_api_utilities):
        # Создаем экземпляр хелпера для работы с авторизацией
        authorization_helper = AuthHelper(auth_api_utilities)
        
        # Генерируем случайные данные для теста
        user_email = faker.email()
        user_password = faker.password(length=8, special_chars=False)
        
        # Создаем DTO для регистрации нового пользователя
        register_dto = Register(
            email=user_email,
            full_name=faker.first_name() + " " + faker.last_name(),
            password=user_password,
            password_repeat=user_password
        )
        
        # Регистрация нового пользователя
        authorization_helper.post_register_user(json=register_dto.model_dump(by_alias=True))

        # Создаем DTO для логина
        login_dto = Login(email=user_email, password=user_password)
        
        # Логинимся под новым пользователем
        login_response = authorization_helper.post_login_user(json=login_dto.model_dump())

        # Получаем статус-код ответа
        actual_status_code = login_response.status_code

        # Проверяем, что статус-код регистрации соответствует ожиданиям
        assert actual_status_code == 201, \
            f"Expected status code: 201 for registration, got: {actual_status_code}"
