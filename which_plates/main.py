"""

Functions
    * which_plates : finds path of least effort
"""
from closet import make_totals, find_closet
from goals import make_goals
from a_star_search import a_star_search
from priority_queue import PriorityQueue
from state import State


def which_plates(goal, plates, percents):
    """Return the path of least weight lifted.

    Description
        given a goal and some plates we find the closest achievable goals,
        their warm up sets, and the path of least effort to them

    Arguments
       goal     : number  : the weight we want to lift
       plates   : Counter : number of plates we have e.g. Counter({15: 2, 10 : 2})
       percents : list    : what percent of our goal lift we want for our warm-up sets

    Returns
       path_of_least_effort: list    : the path of least effort
    """
    all_weights          = make_totals(list(plates.elements()))
    goals                = make_goals(goal, percents)
    closets_goals        = find_closet(all_weights, goals)
    root                 = State.make_start_state(closets_goals, plates)
    final_state          = a_star_search(root, PriorityQueue)
    path_of_least_effort = final_state.path()

    return path_of_least_effort[1:]
