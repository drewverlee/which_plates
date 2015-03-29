"""
contains fixtures, which are used to setup and tear down tests
"""

import pytest
from state import State, Action
from collections import Counter


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

