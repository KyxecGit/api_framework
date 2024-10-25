import logging
import os


class UrlConfig:
    """Класс для хранения URL-адресов API."""

    MOVIE_URL = "https://api.dev-cinescope.store/"  # Базовый URL для работы с фильмами
    AUTH_URL = "https://auth.dev-cinescope.store/"  # URL для аутентификации пользователей
    PAYMENT_URL = "https://payment.dev-cinescope.store/"  # URL для обработки платежей


class LoggerConfig:
    """Класс для настройки конфигурации логирования."""

    LOGGER_NAME = "my_logger"  # Имя логгера
    LOGS_DIR_NAME = "./logs"  # Директория для хранения логов
    LOGS_FILE_NAME = os.path.join(LOGS_DIR_NAME, "app.log")  # Полный путь к файлу логов
    MAX_BYTES = 10 * 1024 * 1024  # Максимальный размер файла логов (10 MB)
    BACKUP_COUNT = 5  # Количество резервных копий логов
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Формат логируемых сообщений
    LOGGER_LEVEL = logging.DEBUG  # Уровень логирования


class CardConfig:
    """Класс для хранения данных карты (например, для тестирования)."""

    CARD_NUMBER = "4242424242424242"  # Номер тестовой карты (Visa)
    DATE = "12/25"  # Дата истечения карты
    CVV = 123  # CVV код тестовой карты
