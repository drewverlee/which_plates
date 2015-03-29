
def test_action(state_4, state_5):
    state = state_4.children()[0]
    assert state.action == state_5.action

def test_node(state_4, state_5):
    state = state_4.children()[0]
    assert state.node() == state_5.node()

def test_plates(state_4, state_5):
    state = state_4.children()[0]
    assert state.plates == state_5.plates

def test_path_cost(state_4, state_5):
    state = state_4.children()[0]
    assert state.path_cost == state_5.path_cost

def test_goals(state_4, state_5):
    state = state_4.children()[0]
    assert state.goals == state_5.goals

def test_goal_i(state_4, state_5):
    state = state_4.children()[0]
    assert state.goal_i == state_5.goal_i

def test_parent(state_4, state_5):
    state = state_4.children()[0]
    assert state.parent == state_5.parent


