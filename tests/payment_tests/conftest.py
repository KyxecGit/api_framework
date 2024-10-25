import pytest

from services.movies.movies_service import MoviesService
from tests.conftest import email, password
from utils.config import UrlConfig
from services.authorization.auth_service import AuthService
from services.authorization.models.auth_model.login import Login
from services.payment.payment_service import PaymentService
from utils.api_util import ApiUtils


@pytest.fixture(scope="session", autouse=False)
def payment_api_service():
    """
    Фикстура для создания анонимного сервиса оплаты.
    """
    anonymous_api_utils = ApiUtils(UrlConfig.PAYMENT_URL)
    api_service = PaymentService(anonymous_api_utils)
    yield api_service


@pytest.fixture(scope="session", autouse=False)
def super_admin_payment_api_service(auth_api_utilities):
    """
    Фикстура для создания сервиса оплаты с правами супер-администратора.
    """
    auth_service = AuthService(url=auth_api_utilities)
    login_dto = Login(email=email, password=password)
    login_response = auth_service.login_user(login_dto)

    api_utils_super_admin = ApiUtils(UrlConfig.PAYMENT_URL, headers={
        "Authorization": f"Bearer {login_response.access_token}"
    })

    api_service = PaymentService(api_utils_super_admin)
    yield api_service


@pytest.fixture(scope="session", autouse=False)
def movie_api_service(movie_api_utilities):
    """
    Фикстура для создания сервиса фильмов.
    """
    api_service = MoviesService(movie_api_utilities)
    yield api_service


@pytest.fixture(scope="session", autouse=False)
def movie_api_utilities(auth_api_utilities):
    """
    Фикстура для создания аутентифицированного доступа к сервису фильмов.
    """
    auth_service = AuthService(url=auth_api_utilities)
    login_dto = Login(email=email, password=password)
    login_response = auth_service.login_user(login_dto)

    api_utils_super_admin = ApiUtils(UrlConfig.MOVIE_URL, headers={
        "Authorization": f"Bearer {login_response.access_token}"
    })

    yield api_utils_super_admin
