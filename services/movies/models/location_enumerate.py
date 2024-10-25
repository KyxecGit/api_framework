from enum import Enum

class LocationEnum(str, Enum):
    """Перечисление для локаций фильмов."""

    SPB = "SPB"  # Санкт-Петербург
    MSK = "MSK"  # Москва
