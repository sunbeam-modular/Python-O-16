# pip install pytest

from math_functions import add, subtract, multiply, divide, is_prime
import pytest

# unit testing add function
def test_add():
    result = add(10, 20)

    # assert the result as 30
    assert(result == 30)

# unit testing subtract function
def test_subtract():
    result = subtract(30, 10)

    # assert the result as 20
    assert(result == 20)

# unit testing divide function
def test_divide():
    result = divide(10, 5)
    assert(result == 2.0)

# unit testing multiply function
def test_multiply():
    result = multiply(10, 20)
    assert(result == 200)


@pytest.mark.parametrize(
    "n, expected", [
        (7, True),
        (11, True),
        (13, True),
        (15, False),
        (17, True),
    ]
)
def test_is_prime(n, expected):
    result = is_prime(n)
    assert(result == expected)
