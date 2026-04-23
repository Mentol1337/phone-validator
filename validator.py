import re

def validate_phone(phone: str) -> bool:
    if not phone:
        raise ValueError("Номер порожній")

    pattern = r"^\+380\d{9}$"
    return bool(re.match(pattern, phone))