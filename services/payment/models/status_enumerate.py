from enum import Enum


class Status(str, Enum):
    """Перечисление статусов платежа."""
    
    SUCCESS = "SUCCESS"
    INVALID_CARD = "INVALID_CARD"
    ERROR = "ERROR"
