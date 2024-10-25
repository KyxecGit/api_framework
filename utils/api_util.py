import json
import curlify
import requests
from requests import Session, RequestException
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .logger import Logger
from .json_util import JsonUtils


def log_response(func):
    """Декоратор для логирования HTTP-запросов и ответов."""
    def _log_response(*args, **kwargs) -> requests.Response:
        try:
            response = func(*args, **kwargs)  # Вызов оригинальной функции для выполнения запроса
            Logger.info(f"Request: {curlify.to_curl(response.request)}")  # Логируем детали запроса

            # Проверяем, является ли ответ JSON и формируем его тело для логирования
            body = json.dumps(response.json(), indent=4) if JsonUtils.is_json(response.text) else response.text
            Logger.info(f"Response: [status_code={response.status_code}, time={response.elapsed}]\n{body}")
            response.raise_for_status()  # Генерируем ошибку для ответов с кодами 4xx и 5xx
            return response
        except RequestException as e:
            Logger.error(f"Request failed: {str(e)}")  # Логируем ошибку, если запрос не удался
            raise e

    return _log_response


class ApiUtils:
    """Утилиты для работы с API, включая управление сессией и повторные запросы."""

    def __init__(self, base_url: str, headers: dict = None, retries: int = 3, 
                 backoff_factor: float = 0.3, status_forcelist: tuple = (500, 502, 504)):
        """
        Инициализация объекта ApiUtils.

        :param base_url: Базовый URL для API
        :param headers: Заголовки для запросов
        :param retries: Количество повторных попыток в случае ошибки
        :param backoff_factor: Фактор задержки между попытками
        :param status_forcelist: Коды статуса, для которых будут повторные попытки
        """
        headers = headers or {}  # Если заголовки не переданы, используем пустой словарь
        self.base_url = base_url
        self.session = Session()
        self.session.headers.update(headers)  # Обновляем заголовки сессии

        # Настройка стратегии повторных попыток для запросов
        retries_strategy = Retry(
            total=retries,  # Общее количество повторов
            backoff_factor=backoff_factor,  # Задержка между попытками
            status_forcelist=status_forcelist,  # Статусы, при которых следует повторять
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"]
        )
        adapter = HTTPAdapter(max_retries=retries_strategy)  # Адаптер с настройками повторных попыток
        self.session.mount("http://", adapter)  # Подключаем адаптер для HTTP
        self.session.mount("https://", adapter)  # Подключаем адаптер для HTTPS

    def update_headers(self, headers: dict) -> None:
        """Обновить заголовки сессии."""
        self.session.headers.update(headers)

    @log_response
    def get(self, endpoint_url: str, **kwargs) -> requests.Response:
        """Выполнение GET запроса по указанному эндпоинту."""
        return self.session.get(self.base_url + endpoint_url, **kwargs)

    @log_response
    def post(self, endpoint_url: str, data=None, json=None, **kwargs) -> requests.Response:
        """Выполнение POST запроса по указанному эндпоинту."""
        return self.session.post(self.base_url + endpoint_url, data=data, json=json, **kwargs)

    @log_response
    def put(self, endpoint_url: str, data=None, **kwargs) -> requests.Response:
        """Выполнение PUT запроса по указанному эндпоинту."""
        return self.session.put(self.base_url + endpoint_url, data=data, **kwargs)

    @log_response
    def delete(self, endpoint_url: str, data=None, **kwargs) -> requests.Response:
        """Выполнение DELETE запроса по указанному эндпоинту."""
        return self.session.delete(self.base_url + endpoint_url, data=data, **kwargs)

    @log_response
    def patch(self, endpoint_url: str, data=None, **kwargs) -> requests.Response:
        """Выполнение PATCH запроса по указанному эндпоинту."""
        return self.session.patch(self.base_url + endpoint_url, data=data, **kwargs)
