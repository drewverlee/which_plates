import pytest
from closest import find_closest_goals, find_closest

@pytest.mark.parametrize(
    "candidates,   goal,     tie_breaker,  expected_closest",  [
    ((0,),      10,  min,          0),
    ((0,),      10,  max,          0),
    ((5,15),    10,  min,          5),
    ((5,15),    10,  max,          15),
    ((5,15),    9,   max,           5),
    ((5,15),    11,  min,          15),
])
def test_find_closest(candidates, goal, tie_breaker, expected_closest):
    assert find_closest(candidates, goal, tie_breaker)  == expected_closest

@pytest.mark.parametrize(
    "candidates,   goals,     tie_breaker,  expected_closest",  [
    [(0,),      (10, 20),  min,          (0, 0)],
    ((0,),      (10, 20),  max,          (0, 0)),
    ((10,),     (10, 20),  min,          (10, 10)),
    ((10,),     (10, 20),  max,          (10, 10)),
    ((10, 20),  (15, 25),  min,          (10, 20)),
    ((10, 20),  (15, 25),  max,          (20, 20)),
])
def test_find_closest_goals(candidates, goals, tie_breaker, expected_closest):
    assert find_closest_goals(candidates, goals, tie_breaker)  == expected_closest
