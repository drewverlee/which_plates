import pytest
from collections import Counter

from main import which_plates
from state import Action


def test_100_with_more_plates():
    plates   = Counter({45:2, 35:2, 25:2, 15:2, 10:2, 5:2, 2.5: 2})
    goal     = 100
    percents = (.20, .40, .60, .80, 1)
    path = which_plates(goal, plates, percents)
    assert path == \
        [
            Action(move='+', weights=[5]),
            Action(move='+', weights=[10]),
            Action(move='+', weights=[5]),
            Action(move='l', weights=[5, 10, 5]),
            Action(move='-', weights=[5]),
            Action(move='+', weights=[25]),
            Action(move='l', weights=[5, 10, 25]),
            Action(move='+', weights=[15]),
            Action(move='+', weights=[5]),
            Action(move='l', weights=[5, 10, 25, 15, 5]),
            Action(move='-', weights=[5]),
            Action(move='+', weights=[25]),
            Action(move='l', weights=[5, 10, 25, 15, 25]),
            Action(move='+', weights=[15]),
            Action(move='+', weights=[5]),
            Action(move='l', weights=[5, 10, 25, 15, 25, 15, 5])
        ]

def test_100_with_less_plates():
    plates   = Counter({45:1, 35:1, 25:1, 15:1, 10:1, 5:1})
    goal     = 100
    percents = (.20, .40, .60, .80, 1)
    path = which_plates(goal, plates, percents)
    assert path == \
        [Action(move='+', weights=[15]),
        Action(move='+', weights=[5]),
        Action(move='l', weights=[15, 5]),
        Action(move='-', weights=[5, 15]),
        Action(move='+', weights=[35]),
        Action(move='+', weights=[5]),
        Action(move='l', weights=[35, 5]),
        Action(move='-', weights=[5]),
        Action(move='+', weights=[25]),
        Action(move='l', weights=[35, 25]),
        Action(move='-', weights=[25]),
        Action(move='+', weights=[45]),
        Action(move='l', weights=[35, 45]),
        Action(move='+', weights=[15]),
        Action(move='+', weights=[5]),
        Action(move='l', weights=[35, 45, 15, 5])]
                
