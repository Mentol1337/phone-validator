import re


def validate_phone(phone: str) -> bool:
    """
    Перевіряє правильність номера телефону у форматі +380XXXXXXXXX.

    Приклади:
    >>> validate_phone("+380991234567")
    True
    >>> validate_phone("0991234567")
    False
    >>> validate_phone("")
    Traceback (most recent call last):
    ...
    ValueError: Номер порожній
    """
    if not phone:
        raise ValueError("Номер порожній")

    pattern = r"^\+380\d{9}$"
    return bool(re.match(pattern, phone))
