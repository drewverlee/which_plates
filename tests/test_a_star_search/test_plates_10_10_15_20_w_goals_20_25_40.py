


def test_action(a_star_search_with_state_start, state_finish):
    state = a_star_search_with_state_start
    assert state.action == state_finish.action

def test_node(a_star_search_with_state_start, state_finish):
    state = a_star_search_with_state_start
    assert state.node() == state_finish.node()

def test_plates(a_star_search_with_state_start, state_finish):
    state = a_star_search_with_state_start
    assert state.plates == state_finish.plates
    
def test_path_cost(a_star_search_with_state_start, state_finish):
    state = a_star_search_with_state_start
    assert state.path_cost == state_finish.path_cost

def test_goals(a_star_search_with_state_start, state_finish):
    state = a_star_search_with_state_start
    assert state.goals == state_finish.goals

def test_goal_i(a_star_search_with_state_start, state_finish):
    state = a_star_search_with_state_start
    assert state.goal_i == state_finish.goal_i

