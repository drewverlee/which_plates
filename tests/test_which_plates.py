import pytest
from collections import Counter

from main import which_plates
from state import _Action


def test_100_with_more_plates():
    plates   = Counter({45:2, 35:2, 25:2, 15:2, 10:2, 5:2, 2.5: 2})
    goal     = 100
    percents = (.20, .40, .60, .80, 1)
    path = which_plates(goal, plates, percents)
    assert path == \
        [
            _Action(move='+', weights=[5]),
            _Action(move='+', weights=[10]),
            _Action(move='+', weights=[5]),
            _Action(move='l', weights=[5, 10, 5]),
            _Action(move='-', weights=[5]),
            _Action(move='+', weights=[25]),
            _Action(move='l', weights=[5, 10, 25]),
            _Action(move='+', weights=[15]),
            _Action(move='+', weights=[5]),
            _Action(move='l', weights=[5, 10, 25, 15, 5]),
            _Action(move='-', weights=[5]),
            _Action(move='+', weights=[25]),
            _Action(move='l', weights=[5, 10, 25, 15, 25]),
            _Action(move='+', weights=[15]),
            _Action(move='+', weights=[5]),
            _Action(move='l', weights=[5, 10, 25, 15, 25, 15, 5])
        ]

def test_100_with_less_plates():
    plates   = Counter({45:1, 35:1, 25:1, 15:1, 10:1, 5:1})
    goal     = 100
    percents = (.20, .40, .60, .80, 1)
    path = which_plates(goal, plates, percents)
    assert path == \
        [_Action(move='+', weights=[15]),
        _Action(move='+', weights=[5]),
        _Action(move='l', weights=[15, 5]),
        _Action(move='-', weights=[5, 15]),
        _Action(move='+', weights=[35]),
        _Action(move='+', weights=[5]),
        _Action(move='l', weights=[35, 5]),
        _Action(move='-', weights=[5]),
        _Action(move='+', weights=[25]),
        _Action(move='l', weights=[35, 25]),
        _Action(move='-', weights=[25]),
        _Action(move='+', weights=[45]),
        _Action(move='l', weights=[35, 45]),
        _Action(move='+', weights=[15]),
        _Action(move='+', weights=[5]),
        _Action(move='l', weights=[35, 45, 15, 5])]
                
