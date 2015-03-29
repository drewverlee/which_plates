


def test_action(a_star_search_with_state_start, state_finish_mocked):
    assert a_star_search_with_state_start.action == state_finish_mocked.action

def test_node(a_star_search_with_state_start, state_finish_mocked):
    assert a_star_search_with_state_start.node() == state_finish_mocked.node()

def test_plates(a_star_search_with_state_start, state_finish_mocked):
    assert a_star_search_with_state_start.plates == state_finish_mocked.plates
    
def test_path_cost(a_star_search_with_state_start, state_finish_mocked):
    assert a_star_search_with_state_start.path_cost == state_finish_mocked.path_cost

def test_goals(a_star_search_with_state_start, state_finish_mocked):
    assert a_star_search_with_state_start.goals == state_finish_mocked.goals

def test_goal_i(a_star_search_with_state_start, state_finish_mocked):
    assert a_star_search_with_state_start.goal_i == state_finish_mocked.goal_i

