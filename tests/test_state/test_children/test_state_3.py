
def test_action(state_3, state_4):
    state = state_3.children()[0]
    assert state.action == state_4.action

def test_node(state_3, state_4):
    state = state_3.children()[0]
    assert state.node() == state_4.node()

def test_plates(state_3, state_4):
    state = state_3.children()[0]
    assert state.plates == state_4.plates

def test_path_cost(state_3, state_4):
    state = state_3.children()[0]
    assert state.path_cost == state_4.path_cost

def test_goals(state_3, state_4):
    state = state_3.children()[0]
    assert state.goals == state_4.goals

def test_goal_i(state_3, state_4):
    state = state_3.children()[0]
    assert state.goal_i == state_4.goal_i

def test_parent(state_3, state_4):
    state = state_3.children()[0]
    assert state.parent == state_4.parent


