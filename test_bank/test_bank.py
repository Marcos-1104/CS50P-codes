from bank import value

import pytest


def test_case_sensitivity():
    assert value("Hello") == 0

def test_starts_with_h():
    assert value("HYper") == 20

def test_other_case():
    assert value("Cars") == 100

def test_omitting_spaces():
    assert value("Hi there") == 20
    assert value ("Hello world!") == 0
    assert value ("red cars") == 100


