import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from typing import Union

from .config import LoggerConfig


class Logger:
    """Класс для настройки и управления логированием."""

    # Создаем директорию для логов, если она не существует
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)

    # Настройка логгера
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)  # Получаем экземпляр логгера с заданным именем
    __logger.setLevel(LoggerConfig.LOGGER_LEVEL)  # Устанавливаем уровень логирования

    # Обработчик для записи логов в файл с ротацией
    __file_handler = RotatingFileHandler(
        LoggerConfig.LOGS_FILE_NAME,  # Путь к файлу логов
        maxBytes=LoggerConfig.MAX_BYTES,  # Максимальный размер файла
        backupCount=LoggerConfig.BACKUP_COUNT  # Количество резервных копий
    )

    # Обработчик для вывода логов в консоль
    __stream_handler = logging.StreamHandler(sys.stdout)

    # Форматирование логируемых сообщений
    __formatter = logging.Formatter(LoggerConfig.FORMAT)
    __file_handler.setFormatter(__formatter)  # Устанавливаем формат для файла
    __stream_handler.setFormatter(__formatter)  # Устанавливаем формат для консоли

    # Добавляем обработчики к логгеру
    __logger.addHandler(__file_handler)
    __logger.addHandler(__stream_handler)

    STEP = 25  # Пользовательский уровень логирования
    logging.addLevelName(STEP, "STEP")  # Добавляем имя для пользовательского уровня

    @staticmethod
    def step(message: str) -> None:
        """Логирование сообщения с пользовательским уровнем STEP."""
        Logger.__logger.log(Logger.STEP, message)

    @staticmethod
    def set_level(level: Union[str, int]) -> None:
        """Устанавливает уровень логирования."""
        Logger.__logger.setLevel(level)

    @staticmethod
    def debug(message: str) -> None:
        """Логирование сообщения уровня DEBUG."""
        Logger.__logger.debug(message)

    @staticmethod
    def info(message: str) -> None:
        """Логирование сообщения уровня INFO."""
        Logger.__logger.info(message)

    @staticmethod
    def warning(message: str) -> None:
        """Логирование сообщения уровня WARNING."""
        Logger.__logger.warning(message)

    @staticmethod
    def error(message: str) -> None:
        """Логирование сообщения уровня ERROR."""
        Logger.__logger.error(message)

    @staticmethod
    def critical(message: str) -> None:
        """Логирование сообщения уровня CRITICAL."""
        Logger.__logger.critical(message)

    @staticmethod
    def fatal(message: str) -> None:
        """Логирование сообщения уровня FATAL."""
        Logger.__logger.fatal(message)

    @staticmethod
    def enable_debug_mode() -> None:
        """Включает режим отладки (DEBUG)."""
        Logger.set_level(logging.DEBUG)

    @staticmethod
    def disable_debug_mode() -> None:
        """Выключает режим отладки (INFO)."""
        Logger.set_level(logging.INFO)
