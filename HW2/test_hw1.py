import pytest

from hw1 import major_and_minor_elem

LISTS = [
    ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ([3, 2, 3], (3, 2)),
    ([3, 3, 2, 2, 3, 3, 1], (3, 1)),
    ([1], (1, 1)),
    ([-10, -10, -5, 0, -10, -99], (-10, -5)),
    ([0, 0, 0, -100, -1000, -100, -100], (0, -1000))
]


@pytest.mark.parametrize(
    "numbers, expected", LISTS
)
def test_major_and_minor_elem(numbers, expected):
    assert major_and_minor_elem(numbers) == expected