import pytest
from working import convert

def test_printing_hours_off():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert ("8:00 PM to 8:00 AM") == "20:00 to 08:00"

def test_printing_minutes_off():
    assert convert ("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert ("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_error_ORG():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60")
        convert("24:90 AM to 25:60 PM")


def test_error():
    with pytest.raises(ValueError):
        convert ("9 AM - 5 PM")

