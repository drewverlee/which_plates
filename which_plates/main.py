"""

Functions
    * which_plates : finds path of least effort
"""
from which_plates.make_totals import _make_totals
from which_plates.closest import _find_closest_goals
from which_plates.goals import _make_goals
from which_plates.a_star_search import _a_star_search
from which_plates.priority_queue import _PriorityQueue
from which_plates.state import _State


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
    all_weights          = _make_totals(list(plates.elements()))
    goals                = _make_goals(goal, percents)
    closets_goals        = _find_closest_goals(all_weights, goals, min)
    root                 = _State.make_start_state(closets_goals, plates)
    final_state          = _a_star_search(root, _PriorityQueue)
    path_of_least_effort = final_state.path()

    return path_of_least_effort[1:]
