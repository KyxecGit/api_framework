import pytest
from faker import Faker
from utils.logger import Logger
from services.authorization.models.user_model.edit_user_dto import EditUser

# Инициализация Faker для генерации тестовых данных
faker = Faker()

class TestChangeUserData:
    # Параметризованный тест для проверки изменения данных пользователя
    @pytest.mark.parametrize("verified, banned", [(False, True)])
    def test_register_user_change_user_data(self, verified, banned, auth_api_service, register_user):
        # Шаг 1: Регистрация нового пользователя
        Logger.info(" !!! Step 1 - Register new user")
        registered_user = register_user  # Получаем информацию о зарегистрированном пользователе

        # Шаг 2: Изменение данных вновь созданного пользователя
        Logger.info(" !!! Step 2 - Change the newly created user data")
        edit_user_dto = EditUser(
            roles=registered_user.user.roles,  # Сохраняем текущие роли пользователя
            verified=verified,  # Устанавливаем новое значение поля verified
            banned=banned  # Устанавливаем новое значение поля banned
        )
        
        # Отправляем PATCH-запрос для изменения данных пользователя
        editing_response = auth_api_service.patch_user(
            user_id=registered_user.user.id,  # Идентификатор пользователя
            edit_user_dto=edit_user_dto  # DTO с изменениями
        )
        
        # Проверяем, что поле banned изменилось как ожидалось
        assert editing_response.banned is banned, \
            f"Expected field banned: {banned} for new created user, got banned: {editing_response.banned} instead"

        # Проверяем, что поле verified изменилось как ожидалось
        assert editing_response.verified is verified, \
            f"Expected verified: {verified} for new created user, got verified: {editing_response.verified} instead"
