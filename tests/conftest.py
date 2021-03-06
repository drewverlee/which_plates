"""
contains fixtures, which are used to setup and tear down tests
"""

import pytest
from os import environ
from mock import MagicMock
from collections import Counter

from state import _State, _Action
from priority_queue import _PriorityQueue
from a_star_search import _a_star_search

# see the readme in the test_children directory for an explanation of the
# setups

@pytest.fixture(scope="module")
def state_0():
    """Create the start state"""
    action    = _Action("", [])
    bar       = []
    plates    = Counter({20: 1, 25: 1})
    path_cost = 0
    path_used = 0
    goals     = (20, 25, 0)
    goal_i    = 0
    parent    = None

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_1(state_0):
    action    = _Action("+", [20])
    bar       = [20]
    plates    = Counter({20: 0, 25: 1})
    path_cost = 0
    path_used = 1
    goals     = (20, 25, 0)
    goal_i    = 0
    parent    = state_0

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_2(state_1):
    action    = _Action("l", [20])
    bar       = [20]
    plates    = Counter({20: 0, 25: 1})
    path_cost = 0
    path_used = 1
    goals     = (20, 25, 0)
    goal_i    = 1
    parent    = state_1

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_3(state_2):
    action    = _Action("-", [20])
    bar       = []
    plates    = Counter({20: 1, 25: 1})
    path_cost = 20
    path_used = 2
    goals     = (20, 25, 0)
    goal_i    = 1
    parent    = state_2

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_4(state_3):
    action    = _Action("+", [25])
    bar       = [25]
    plates    = Counter({20: 1, 25: 0})
    path_cost = 20
    path_used = 3
    goals     = (20, 25, 0)
    goal_i    = 1
    parent    = state_3

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_5(state_4):
    action    = _Action("l", [25])
    bar       = [25]
    plates    = Counter({20: 1, 25: 0})
    path_cost = 20
    path_used = 3
    goals     = (20, 25, 0)
    goal_i    = 2
    parent    = state_4

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)


@pytest.fixture()
def priority_queue():
    return _PriorityQueue([])


@pytest.fixture(scope="module")
def priority_queue_with_items(mock_item_one, mock_item_two):
    return _PriorityQueue([mock_item_one, mock_item_two])


@pytest.fixture(scope="module")
def mock_item_one():
    def side_effect(): 
        return 1
    item_one = MagicMock()
    item_one.priority = side_effect
    return item_one


@pytest.fixture(scope="module")
def mock_item_two():
    def side_effect(): 
        return 2
    item_two = MagicMock()
    item_two.priority = side_effect
    return item_two


@pytest.fixture(scope="module")
def a_star_search_with_state_0(state_0):
    return _a_star_search(state_0, _PriorityQueue)


# actual problem setup
@pytest.fixture(scope="module")
def state_start():
    action    = _Action("", [])
    bar       = []
    plates    = Counter({20: 1, 25: 1, 15: 1, 10: 2})
    path_cost = 0
    path_used = 0
    goals     = (20, 25, 40, 0)
    goal_i    = 0
    parent    = None

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)

@pytest.fixture(scope="module")
def state_finish_mocked():
    action    = _Action("l", [25, 15])
    bar       = [25, 15]
    plates    = Counter({20: 1, 25: 0, 15: 0, 10: 2})
    path_cost = 20
    path_used = 4
    goals     = (20, 25, 40, 0)
    goal_i    = 3
    parent    = MagicMock # TODO do we want to test parent?

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)


@pytest.fixture(scope="module")
def a_star_search_with_state_start(state_start):
    return _a_star_search(state_start, _PriorityQueue)

@pytest.fixture(scope="module")
def state_start_large():
    action    = _Action("", [])
    bar       = []
    plates    = Counter({
        1   : 2,
        2.5 : 3,
        5   : 3,
        10  : 3,
        15  : 3,
        25  : 3,
        35  : 3,
        45  : 6,
    })
    path_cost = 0
    path_used = 0
    goals     = (40, 80, 120, 160, 200, 0)
    goal_i    = 0
    parent    = None

    return _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)

    
@pytest.fixture(scope="module")
def states_for_timming():
    states = []
    N = 5
    for n in range(1, N):
        action    = _Action("", [])
        bar       = []
        plates    = Counter({
            1 : n,
            2 : n, 
            3 : n, 
            4 : n, 
            5 : n, 
            6 : n, 
            7 : n, 
            8 : n, 
            9 : n
        })
        path_cost = 0
        path_used = 0
        goals     = tuple((n*10)*p for p in [.20, .40, .60, .80, 1]) + (0,)
        goal_i    = 0
        parent    = None
        state_start = _State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)
        states.append(state_start)
    return states


