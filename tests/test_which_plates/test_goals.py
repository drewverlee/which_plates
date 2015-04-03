import pytest
from goals import make_goals

@pytest.mark.parametrize(
    "goal,  percentages,                 expected_goals", [
    (100,   (1,),                         (100,)),
    (100,   (0, 0.2, 0.4, 0.6, 0.8, 1),  (0, 20, 40, 60, 80, 100)),
])
def test_make_goals(goal, percentages, expected_goals):
    assert make_goals(goal, percentages) == expected_goals
