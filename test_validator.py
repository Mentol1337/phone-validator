from validator import validate_phone
import pytest


def test_valid():
    assert validate_phone("+380991234567") == True


def test_invalid():
    assert validate_phone("0991234567") == False


def test_empty():
    with pytest.raises(ValueError):
        validate_phone("")
