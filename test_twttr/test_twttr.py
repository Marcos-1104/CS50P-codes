import pytest

from twttr import shorten

def test_Uppercase():
    assert shorten ("TwIttEr") == "Twttr"

def test_lowercase():
    assert shorten ("Twitter")  == "Twttr"

def test_error():
     with pytest.raises(TypeError):
         shorten(1)

def test_punctuation():
    assert shorten("Twi.tter.") == "Tw.ttr."

def test_numbers():
    assert shorten("Twi1tte2r") == "Tw1tt2r"
