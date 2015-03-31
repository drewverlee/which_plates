"""
Description
    Contains the functionality for finding all the closets possible
    goals to our original goals.

Functions
    * make_totals : Makes all possible totals from a bag of numbers
    * next_gen    : Makes the next set of numbers based on the parent
        generation
    * closet      : Finds the closet number to a goal in a set of goals
"""


def make_totals(bag):
    """Makes all possible totals from a bag of numbers

    Description
        Given a list of numbers were able to find all possible 'totals' that
        can be made by summing up every possible combination.

    Example
        >>> make_totals([1,2])
        {0, 1, 2, 3}

    Arguments
        * bag  : list : a multiset of numbers

    Returns
        totals : set  : all possible totals
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
    return totals


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


def find_closet(numbers, goals, tie_breaker=min):
    """Finds the closet number to a goal in a set of goals

    Description
        Given a set of numbers and goals we pick from amongst all the numbers
            to get as close to the goals as possible, breaking ties using the
            tie breaker.

    Example
        >>> find_closet([1,3], [2], min)
        [1]

    Arguments
        * numbers     : list : Numbers we can draw choose between.
        * goals       : list : A list of the numbers were trying to get as close
            to as possible.
        * tie_breaker : func : How to break ties when were equally close above
            and below a goal.
    Returns
        closets       : list : A list of numbers that are as close to the goals
            as we can get given the numbers provided.
    """
    above  = [float('inf')] * len(goals)
    below  = [float('inf')] * len(goals)
    closet = [None] * len(goals)

    for i, goal in enumerate(goals):
        for num in numbers:
            possible_closet = goal - num
            if possible_closet == 0:
                above[i], below[i] = num, num
            elif possible_closet > 0 and abs(possible_closet) < below[i]:
                below[i] = num
            elif possible_closet < 0 and abs(possible_closet) < above[i]:
                above[i] = num

    for i in range(len(goals)):
        if abs(above[i] - goals[i]) == abs(below[i] - goals[i]):
            closet[i] = tie_breaker(above[i], below[i])
        else:
            closet[i] = min(above[i], below[i])
    return closet
