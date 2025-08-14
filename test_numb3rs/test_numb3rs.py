from numb3rs import validate

import pytest

def more_than():
    assert validate("512.512.512.512") == False
    assert validate("140.247.235.144") == False

def valid():
    assert validate("127.0.0.1") == True

def whole_octect():
    assert validate("255.255.255.255") == True

def word_ip():
    assert validate("cat") == False

def only_zero():
    assert validate("0.0.0.0") == True


