
def test_action(state_0, state_1):
    state = state_0.children()[0]
    assert state.action == state_1.action

def test_node(state_0, state_1):
    state = state_0.children()[0]
    assert state.node() == state_1.node()

def test_plates(state_0, state_1):
    state = state_0.children()[0]
    assert state.plates == state_1.plates

def test_path_cost(state_0, state_1):
    state = state_0.children()[0]
    assert state.path_cost == state_1.path_cost

def test_goals(state_0, state_1):
    state = state_0.children()[0]
    assert state.goals == state_1.goals

def test_goal_i(state_0, state_1):
    state = state_0.children()[0]
    assert state.goal_i == state_1.goal_i

def test_parent(state_0, state_1):
    state = state_0.children()[0]
    assert state.parent == state_1.parent


