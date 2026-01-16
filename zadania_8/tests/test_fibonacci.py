import pytest
from zadania_8.main import fibonacci

@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
    ],
)

def test_is_palindrome(n, expected):
    assert fibonacci(n) == expected

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)