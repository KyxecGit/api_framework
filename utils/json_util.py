import json


class JsonUtils:
    """Утилиты для работы с JSON данными."""

    @staticmethod
    def is_json(file: str) -> bool:
        """Проверяет, является ли строка корректным JSON.

        :param file: Строка, которую нужно проверить на валидность JSON
        :return: True, если строка является корректным JSON, иначе False
        """
        try:
            json.loads(file)  # Пытаемся загрузить строку как JSON
        except ValueError:
            return False  # Возвращаем False, если произошла ошибка
        return True  # Если загрузка успешна, возвращаем True
