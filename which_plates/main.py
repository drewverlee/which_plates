"""
contains

* main : given a goal and some plates we find the closest achievable goals,
    their warm up sets, and the path of least effort to them
"""

from closet import make_totals, find_closet
from goals import make_goals
from a_star_search import a_star_search
from priority_que import PriorityQue
from state import State

# #TODO make sure we have "returns" everywhere
# #TODO add docstring tests to main at least
# #TODO list vs tuple 
# #TODO plates should be a Counter all the way through... 

#TODO make it take command line arguments
def main(goal, plates, percents=[0.2, 0.4, 0.6, 0.8, 1]):
    """return path of least effort

    :goal: number: the weight we want to lift
    :plates: Counter: number of plates we have e.g. Counter({15: 2, 10: 2})
    :percents: list: what percent of our goal lift we want for our warm-up sets
    :returns: list: path of least effort 
    """
    all_weights = make_totals(list(plates.elements()))
    goals = make_goals(goal, percents)
    closets_goals = find_closet(all_weights, goals)
    root = State.make_start_state(goals, plates)
    final_state = a_star_search(root, PriorityQue)
    path_of_least_effort = final_state.path()
    
    return path_of_least_effort[1:]



    
