
def test_action(state_2, state_3):
    state = state_2.children()[0]
    assert state.action == state_3.action

def test_node(state_2, state_3):
    state = state_2.children()[0]
    assert state.node() == state_3.node()

def test_plates(state_2, state_3):
    state = state_2.children()[0]
    assert state.plates == state_3.plates

def test_path_cost(state_2, state_3):
    state = state_2.children()[0]
    assert state.path_cost == state_3.path_cost

def test_goals(state_2, state_3):
    state = state_2.children()[0]
    assert state.goals == state_3.goals

def test_goal_i(state_2, state_3):
    state = state_2.children()[0]
    assert state.goal_i == state_3.goal_i

def test_parent(state_2, state_3):
    state = state_2.children()[0]
    assert state.parent == state_3.parent


