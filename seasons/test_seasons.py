from seasons import Person
from datetime import date
import pytest


def test_handle_valid_dates():
    person = Person.handle_date("1999-01-01")
    assert person.birthdate == date(1999,1,1)

def test_handle_invalid_dates():

    with pytest.raises(SystemExit):
        Person.handle_date("Januaary 1,1999")
    with pytest.raises(SystemExit):
        Person.handle_date("2000-14-12")
    with pytest.raises(SystemExit):
        Person.handle_date("2000-04-32")
    with pytest.raises(SystemExit):
        Person.handle_date("2000/12/30")

def test_age_in_minutes_calculation():
    birthdate = date(2000, 4, 11)
    p = Person(birthdate)
    fixed_today = date(2025,7,17)
    age = fixed_today - birthdate
    expected_minutes = age.days*24*60

    assert p.age_in_minutes(today=fixed_today) == expected_minutes
