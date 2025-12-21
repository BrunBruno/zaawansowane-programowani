import pytest
from zadania_8.main import calculate_discount

@pytest.mark.parametrize(
    "price,discount,expected",
    [
        (100,0.2,80.0),
        (50,0,50.0),
        (200,1,0.0),
    ],
)

def test_calculate_discount(price, discount, expected):
    assert calculate_discount(price,discount) == expected

def test_calculate_discount_negative():
    with pytest.raises(ValueError):
        calculate_discount(100, -1)
        calculate_discount(100, 1.5)