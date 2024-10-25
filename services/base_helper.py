from utils.config import UrlConfig


class BaseHelper:
    def __init__(self, url: UrlConfig):
        """Инициализация базового помощника с URL конфигурацией."""
        self.url = url
