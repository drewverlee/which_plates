"""
Description
    Contains functionality for finding all possible totals from a bag of numbers.

Functions
    * _make_totals : Makes all possible totals from a bag of numbers.
    * _next_gen    : Makes the next set of numbers based on the parent
        generation

"""
def _make_totals(bag):
    """Makes all possible totals from a bag of numbers

    Description
        Given a list of numbers were able to find all possible 'totals' that
        can be made by summing up every possible combination.

    Example
        >>> _make_totals([1,2])
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
        generations.append(_next_gen(generations[-1], bag, closed))
        totals.update(generations[-1])
    return sorted(list(totals))


def _next_gen(parent_gen, bag, closed):
    """Makes the next set of numbers based on the parent generation

    Description
        Given a parent generation to build upon it creates the next
        generation of totals we can make from our bag. The optimization
        over taking every combination comes when we skip totals we have seen
        in the closed set before and don't expand them again.

    Example
        >>> _next_gen({1 : {0}, 2: {1}}, [1, 2], {1, 2})
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
