import pytest
from scripts.tuple_demo import min_max

@pytest.mark.parametrize("numbers, expected", [
    ([3, 1, 4, 1, 5, 9], (1, 9)),
    ([0], (0, 0)),
    ([-5, -10, 0, 5], (-10, 5)),
    ([2, 2, 2], (2, 2)),
])
def test_min_max(numbers, expected):
    assert min_max(numbers) == expected

def test_min_max_empty():
    with pytest.raises(ValueError):
        min_max([])
