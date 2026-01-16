import pytest
from zadania_8.main import flatten_list

@pytest.mark.parametrize(
    "list_in,list_out",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([1, [2, 3], [4, [5]]], [1, 2, 3, 4, 5]),
        ([],[]),
        ([[[1]]], [1]),
        ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
    ],
)

def test_flatten_list(list_in,list_out):
    assert flatten_list(list_in) == list_out

