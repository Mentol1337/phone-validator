from validator import validate_phone
import pytest


def test_valid():
    assert validate_phone("+380991234567")


def test_invalid():
    assert not validate_phone("0991234567")


def test_empty():
    with pytest.raises(ValueError):
        validate_phone("")
