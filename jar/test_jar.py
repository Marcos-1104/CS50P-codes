from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(capacity=20)
    assert jar.capacity == 20

    with pytest.raises(ValueError):
        Jar(capacity=-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(5)
    assert jar.size == 11
    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw():

    # Setup the jar by depositing cookies first
    jar = Jar()
    jar.deposit(10)

    # Test a valid withdrawal
    jar.withdraw(4)
    assert jar.size == 6

    # Test withdrawing more cookies than are in the jar
    with pytest.raises(ValueError):
        jar.withdraw(7)  # 7 > 6, so this should fail

    # Test withdrawing from a new, empty jar
    empty_jar = Jar()
    with pytest.raises(ValueError):
        empty_jar.withdraw(1)


