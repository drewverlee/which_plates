import pytest
from closet import find_closet

@pytest.mark.parametrize(
    "numbers,   goals,     tie_breaker,  expected_closet",  [
    ((0,),      (10, 20),  min,          [0, 0]),
    ((0,),      (10, 20),  max,          [0, 0]),
    ((10,),     (10, 20),  min,          [10, 10]),
    ((10,),     (10, 20),  max,          [10, 10]),
    ((10, 20),  (15, 25),  min,          [10, 20]),
    ((10, 20),  (15, 25),  max,          [20, 20]),
])
def test_find_closets(numbers, goals, tie_breaker, expected_closet):
    assert find_closet(numbers, goals, tie_breaker) == expected_closet