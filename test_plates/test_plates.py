import pytest
from plates import is_valid


def test_start_two_letters():
    assert is_valid("AAA222") == True
    assert is_valid("A2AA22") == False
    assert is_valid("3AAA22") == False
    assert is_valid("50") == False
    assert is_valid("32AA22") == False
    assert is_valid("@3!ABC") == False

def test_lenght():
    assert is_valid("A") == False
    assert is_valid("AAAAAAAAA") == False

def test_middle_numbers():
    assert is_valid("AA22AA") == False
    assert is_valid("AAA22A") == False


def test_first_number():
    assert is_valid("AA022A") == False
    assert is_valid("AAAb02") == False
    assert is_valid("AAABB0") == False
    assert is_valid("AA0234") == False


def test_punctuation():
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("Hello@, World") == False
    assert is_valid("AA123!") == False  # Contains an exclamation mark
    assert is_valid("AA 123") == False  # Contains a space


