
def test_action(state_1, state_2):
    state = state_1.children()[0]
    assert state.action == state_2.action

def test_node(state_1, state_2):
    state = state_1.children()[0]
    assert state.node() == state_2.node()

def test_plates(state_1, state_2):
    state = state_1.children()[0]
    assert state.plates == state_2.plates

def test_path_cost(state_1, state_2):
    state = state_1.children()[0]
    assert state.path_cost == state_2.path_cost

def test_goals(state_1, state_2):
    state = state_1.children()[0]
    assert state.goals == state_2.goals

def test_goal_i(state_1, state_2):
    state = state_1.children()[0]
    assert state.goal_i == state_2.goal_i

def test_parent(state_1, state_2):
    state = state_1.children()[0]
    assert state.parent == state_2.parent


