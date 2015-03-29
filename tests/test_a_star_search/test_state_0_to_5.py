

def test_action(a_star_search_with_state_0, state_5):
    assert a_star_search_with_state_0.action == state_5.action

def test_node(a_star_search_with_state_0, state_5):
    assert a_star_search_with_state_0.node() == state_5.node()

def test_plates(a_star_search_with_state_0, state_5):
    assert a_star_search_with_state_0.plates == state_5.plates
    
def test_path_cost(a_star_search_with_state_0, state_5):
    assert a_star_search_with_state_0.path_cost == state_5.path_cost

def test_goals(a_star_search_with_state_0, state_5):
    assert a_star_search_with_state_0.goals == state_5.goals

def test_goal_i(a_star_search_with_state_0, state_5):
    assert a_star_search_with_state_0.goal_i == state_5.goal_i

# TODO
# not sure about this failing, maybe need to define equals on state
# def test_parent(a_star_search_with_state_0, state_5):
#     state = a_star_search_with_state_0
#     assert state.parent == state_5.parent

