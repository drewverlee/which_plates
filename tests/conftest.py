"""
contains fixtures, which are used to setup and tear down tests
"""

import pytest
from mock import MagicMock
from collections import Counter

from state import State, Action
from priority_que import PriorityQue
from a_star_search import a_star_search


# see the readme in the test_children directory for an explanation of the
# setups

@pytest.fixture(scope="module")
def state_0():
    """Create the start state"""
    action    = Action("", [])
    bar       = []
    plates    = Counter({20: 1, 25: 1})
    path_cost = 0
    goals     = (20, 25, 0)
    goal_i    = 0
    parent    = None

    return State(action, bar, plates, path_cost, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_1(state_0):
    action    = Action("+", [20])
    bar       = [20]
    plates    = Counter({20: 0, 25: 1})
    path_cost = 0
    goals     = (20, 25, 0)
    goal_i    = 0
    parent    = state_0

    return State(action, bar, plates, path_cost, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_2(state_1):
    action    = Action("l", [20])
    bar       = [20]
    plates    = Counter({20: 0, 25: 1})
    path_cost = 0
    goals     = (20, 25, 0)
    goal_i    = 1
    parent    = state_1

    return State(action, bar, plates, path_cost, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_3(state_2):
    action    = Action("-", [20])
    bar       = []
    plates    = Counter({20: 1, 25: 1})
    path_cost = 20
    goals     = (20, 25, 0)
    goal_i    = 1
    parent    = state_2

    return State(action, bar, plates, path_cost, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_4(state_3):
    action    = Action("+", [25])
    bar       = [25]
    plates    = Counter({20: 1, 25: 0})
    path_cost = 20
    goals     = (20, 25, 0)
    goal_i    = 1
    parent    = state_3

    return State(action, bar, plates, path_cost, goals, goal_i, parent)


@pytest.fixture(scope="module")
def state_5(state_4):
    action    = Action("l", [25])
    bar       = [25]
    plates    = Counter({20: 1, 25: 0})
    path_cost = 20
    goals     = (20, 25, 0)
    goal_i    = 2
    parent    = state_4

    return State(action, bar, plates, path_cost, goals, goal_i, parent)


@pytest.fixture()
def priority_que():
    return PriorityQue([])


@pytest.fixture(scope="module")
def priority_que_with_items(mock_item_one, mock_item_two):
    return PriorityQue([mock_item_one, mock_item_two])


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
    return a_star_search(state_0, PriorityQue)

# actual problem setup

@pytest.fixture(scope="module")
def state_start():
    action    = Action("", [])
    bar       = []
    plates    = Counter({20: 1, 25: 1, 15: 1, 10: 2})
    path_cost = 0
    goals     = (20, 25, 40, 0)
    goal_i    = 0
    parent    = None

    return State(action, bar, plates, path_cost, goals, goal_i, parent)

@pytest.fixture(scope="module")
def state_finish():
    action    = Action("l", [25, 15])
    bar       = [25, 15]
    plates    = Counter({20: 1, 25: 0, 15: 0, 10: 2})
    path_cost = 20
    goals     = (20, 25, 40, 0)
    goal_i    = 3
    parent    = MagicMock # TODO do we want to test parent?

    return State(action, bar, plates, path_cost, goals, goal_i, parent)

@pytest.fixture(scope="module")
def a_star_search_with_state_start(state_start):
    return a_star_search(state_start, PriorityQue)








