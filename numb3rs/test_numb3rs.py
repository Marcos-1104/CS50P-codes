from numb3rs import validate

import pytest

def test_more_than():
    assert validate("512.512.512.512") == False
    assert validate("140.247.235.144") == True
    assert validate("192.512.144.250") == False
    assert validate("192.112.544.250") == False
    assert validate("192.112.144.550") == False
    assert validate("192.112.144.259") == False

def test_valid():
    assert validate("127.0.0.1") == True

def test_whole_octect():
    assert validate("255.255.255.255") == True

def test_word_ip():
    assert validate("cat") == False

def test_only_zero():
    assert validate("0.0.0.0") == True


