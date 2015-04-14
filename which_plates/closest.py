"""
Description
    Contains the functionality for finding all the closest possible
    goals to our original goals.

Functions
    * _make_totals : Makes all possible totals from a bag of numbers
    * _next_gen    : Makes the next set of numbers based on the parent
        generation
    * _find_closest      : Finds the closest number to a goal in a set of goals
"""
from bisect import bisect_left


def make_totals(bag):
    """Makes all possible totals from a bag of numbers

    Description
        Given a list of numbers were able to find all possible 'totals' that
        can be made by summing up every possible combination.

    Example
        >>> make_totals([1,2])
        [0, 1, 2, 3]

    Arguments
        * bag  : list : a multiset of numbers

    Returns
        totals : list  : ordered totals
    """
    start = {}
    EMPTY_SET_TOTAL = 0
    start = {EMPTY_SET_TOTAL: set()}
    generations = [start]
    closed = {EMPTY_SET_TOTAL}
    totals = set([0])
    while len(generations) <= len(bag):
        generations.append(next_gen(generations[-1], bag, closed))
        totals.update(generations[-1])
    return sorted(list(totals))


def next_gen(parent_gen, bag, closed):
    """Makes the next set of numbers based on the parent generation

    Description
        Given a parent generation to build upon it creates the next
        generation of totals we can make from our bag. The optimization
        over taking every combination comes when we skip totals we have seen
        in the closed set before and don't expand them again.

    Example
        >>> next_gen({1 : {0}, 2: {1}}, [1, 2], {1, 2})
        {3: {0, 1}}

    Arguments
        * parent_gen : dict : values represent the indices of the  numbers in
            the bag for example a parent generation key with {0, 1} could have
            a bag like [5, 5] and so its key would be 10. e.g parent_gen[10] =
            [0, 1]
        * bag        : list : a multiset of numbers
        * closed     : set  : totals we have seen already and so can skip.

    Returns
        nxt_gen    : dict  : like the parent generation, the next generation is
        a dictionary with keys represented by a sum of the numbers in the bag
        which you can index by the values.
    """
    nxt_gen = dict()

    for total, indices in parent_gen.items():
        for i, num in enumerate(bag):
            new_total = num + total
            if new_total not in closed and i not in indices:
                closed.add(new_total)
                new_index = indices.copy()
                new_index.add(i)
                nxt_gen[new_total] = new_index

    return nxt_gen





def find_closest(candidates, goal, tie_breaker=min):
    """Finds the closest number to a goal in a set of goals

    Description
        Given a set of numbers and goals we pick from amongst all the numbers
            to get as close to the goals as possible, breaking ties using the
            tie breaker.

    Example
        >>> find_closest([1,3], 2, min)
        (1,)

    Arguments
        * numbers     : tuple : a sorted list of candidate numbers we can draw choose between.
        * goals       : tuple : A list of the numbers were trying to get as close
            to as possible.
        * tie_breaker : func : How to break ties when were equally close above
            and below a goal.
    Returns
        closests       : tuple : A list of numbers that are as close to the goals
            as we can get given the numbers provided.
    """
    pos = bisect_left(candidates, goal)
    before = candidates[pos - 1]
    after = candidates[pos]
    if pos == 0:
        return candidates[0]
    elif pos == len(candidates):
        return candidates[-1]
    elif candidates[pos] == goal: 
        return goal
    elif after - goal < goal - before:
       return after
    else:
       return tie_breaker(after, before)
