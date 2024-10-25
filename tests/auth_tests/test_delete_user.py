import requests
from faker import Faker
from utils.logger import Logger
from services.authorization.models.auth_model.login import Login

# Инициализация Faker для генерации тестовых данных
faker = Faker()

class TestDeleteUser:
    def test_register_and_delete_user(self, auth_api_service, auth_api_utilities, register_user):
        # Шаг 1: Регистрация нового пользователя
        Logger.info(" !!! Step 1 - Register new user")
        registered_user_info = register_user

        # Извлекаем информацию о зарегистрированном пользователе
        registered_user = registered_user_info.user
        password = registered_user_info.password
        email = registered_user_info.email

        # Шаг 2: Логин под новым пользователем
        Logger.info(" !!! Step 2 - Log in as new user")
        auth_api_service.update_api_utils(token=None)  # Сбрасываем токен
        login_dto = Login(email=email, password=password)  # DTO для логина
        login_response = auth_api_service.login_user(login_dto=login_dto)  # Выполняем логин

        # Шаг 3: Удаление пользователя
        Logger.info(" !!! Step 3 - Delete new user")
        auth_api_service.update_api_utils(token=login_response.access_token)  # Обновляем токен для авторизованного пользователя
        auth_api_service.delete_user(registered_user.id)  # Удаляем пользователя

        # Шаг 4: Проверка, что логин недоступен после удаления
        Logger.info("Шаг 4 - Подтверждение, что логин невозможен после удаления")

        # Сбрасываем токен для нового логина
        auth_api_service.update_api_utils(token=None)

        # Пытаемся залогиниться и ожидаем ошибку
        try:
            failed_login_response = auth_api_service.login_user(login_dto=login_dto)  # Пытаемся выполнить логин
            failed_login_response.raise_for_status()  # Проверяем статус ответа

        except requests.exceptions.HTTPError as err:
            # Обработка ошибки HTTP
            actual_status_code = err.response.status_code  # Получаем статус-код ошибки
            expected_status_code = requests.status_codes.codes.unauthorized  # Ожидаемый статус код

            Logger.error(f"Ошибка при попытке логина: {err}")  # Логируем ошибку
            # Проверяем, что статус-код соответствует ожиданиям
            assert actual_status_code == expected_status_code, \
                f"Ожидался статус {expected_status_code}, а получен {actual_status_code}"

            Logger.info(f"Шаг 4 завершён. Логин невозможен, как и ожидалось. Статус: {actual_status_code}")  # Логируем успешное завершение шага
