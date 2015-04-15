"""
Description
    Contains the functionality for finding all the candidates numbers
    that are closest to our goals.

Functions
    * _find_closest      : Finds the closest number to a goal in a set of goals

"""
from bisect import bisect_left


def _find_closest(candidates, goal, tie_breaker=min):
    """Finds the closest candidate to a goal in a set of goals

    Description
        Given a set of candidates and goals we pick from amongst all the candidates
            to get as close to the goals as possible, breaking ties using the
            tie breaker.

    Example
        >>> _find_closest([1,3], 2, min)
        1

    Arguments
        * candidates     : tuple : a sorted list of candidate candidates we can draw choose between.
        * goals       : tuple : A list of the candidates were trying to get as close
            to as possible.
        * tie_breaker : func : How to break ties when were equally close above
            and below a goal.
    Returns
        closest       : tuple : A list of candidates that are as close to the goals
            as we can get given the candidates provided.
    """
    pos = bisect_left(candidates, goal)

    if pos == len(candidates):
        return candidates[-1]
    elif candidates[pos] == goal:
        return goal
    else:
        before = candidates[pos - 1]
        after = candidates[pos]

        before_distance = abs(goal - before)
        after_distance = abs(goal - after)

        if before_distance == after_distance:
            return tie_breaker(before, after)
        elif before_distance < after_distance:
            return before
        else:
            return after


def _find_closest_goals(candidates, goals, tie_breaker):
    """Return a list of candidates closest to a list of goals."""
    return tuple([_find_closest(candidates, goal, tie_breaker) for goal in goals])
    
