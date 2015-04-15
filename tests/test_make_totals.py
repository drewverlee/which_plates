import pytest
from make_totals import _make_totals

@pytest.mark.parametrize(
    "bag,               expected_totals",  [
    ((),                [0]),
    ((1,),               [0, 1]),
    ((3, 5),            [0, 3, 5, 8]),
    ((1, 2),            [0, 1, 2, 3]),
    ((10, 20, 30, 40),  [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
])
def test_make_totals(bag, expected_totals):
    assert _make_totals(bag) == expected_totals


