import pytest
from zadania_8.main import count_vowels

@pytest.mark.parametrize(
    "text,expected",
    [
        ("Python", 2),
        ("AEIOUY", 6),
        ("", 0),
        ("bcd", 0),
        ("Próba żółwia", 4),
    ],
)

def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
