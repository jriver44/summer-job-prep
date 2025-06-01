import pytest
from scripts.unique_demo import parse_input_to_int_list, unique_sorted

def test_parse_input_to_int_list_valid():
    assert parse_input_to_int_list("3 1 4 1 5 9") == [3, 1, 4, 1, 5, 9]
    assert parse_input_to_int_list("  10  -2  5  ") == [10, -2, 5]

def test_parse_input_to_int_list_invalid():
    with pytest.raises(ValueError):
        parse_input_to_int_list("3 a 4")

@pytest.mark.parametrize("numbers, expected", [
    ([3, 1, 4, 1, 5, 9], [1, 3, 4, 5, 9]),
    ([], []),
    ([2, 2, 2], [2]),
    ([5, -1, 0, -1], [-1, 0, 5]),
])
def test_unique_sorted(numbers, expected):
    assert unique_sorted(numbers) == expected
