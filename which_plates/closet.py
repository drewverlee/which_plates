"""

* totals: uses dynamic programming to find all the sums of a bag

"""
from collections import defaultdict


def make_totals(bag):
    """finds the totals for all combinations of the numbers in bag

    :bag: a bag of numbers
    :returns: a set of totals
    """
    start = defaultdict(set)
    EMPTY_SET_TOTAL = 0
    start[EMPTY_SET_TOTAL] = set()
    generations = [start]
    closed = {EMPTY_SET_TOTAL}
    totals = set([0])
    while len(generations) <= len(bag):
        generations.append(next_gen(generations[-1], bag, closed))
        totals.update(generations[-1])
    return totals


def next_gen(parent_gen, bag, closed):
    """find the next set of numbers based on the parent_gen

    :parent_gen: set of totals possible in last generation
    :bag: bag of numbers
    :closed: totals we have seen already
    :returns: set of totals possible this generation
    """
    nxt_gen = defaultdict(set)
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
    """finds the cloests number to a goal in a set of goals

    :numbers: some numbers
    :goals: numbers were hopeing to get close to
    :tie_breaker: high or low, i.e with a goal of 15 and numbers 10, 20 do we 
        choose 10 or 20
    :returns: list of closets numbers to the goals

    """
    above  = [float('inf')] * len(goals)
    below  = [float('inf')] * len(goals)
    closet = [None] * len(goals)

    for i, goal in enumerate(goals):
        for num in numbers:
            c = goal - num
            if c == 0:
                above[i], below[i] = num, num
            elif c > 0 and abs(c) < below[i]:
                below[i] = num
            elif c < 0 and abs(c) < above[i]:
                above[i] = num
    
    for i in range(len(goals)):
        if abs(above[i] - goals[i]) == abs(below[i] - goals[i]):
            closet[i] = tie_breaker(above[i], below[i])
        else:
            closet[i] = min(above[i], below[i])
    return closet


