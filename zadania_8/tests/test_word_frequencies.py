import pytest
from zadania_8.main import word_frequencies

@pytest.mark.parametrize(
    "text,result",
    [
        ("To be or not to be", {"to": 2, "be": 2, "or": 1, "not": 1}),
        ("Hello, hello!", {"hello": 2}),
        ("", {}),
        ("Python Python python", {"python": 3}),
        ("Ala ma kota, a kot ma Ale.", {"ala":1,"ma":2,"kota":1,"kot":1,"ale":1,"a":1}),
    ],
)

def test_word_frequencies(text, result):
    assert word_frequencies(text) == result
