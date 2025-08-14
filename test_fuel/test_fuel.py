import pytest

from fuel import convert
from fuel import gauge


def test_interger():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("1.5/3")


def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_output():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"


def test_icorrect_ints():
    assert convert("2/3") == 67
    assert convert ("1/3") == 33
