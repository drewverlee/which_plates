"""
contains:

* make_goals
* 
"""
def make_goals(goal, percentages=[0.2, 0.4, 0.6, 0.8]):
    """From a final goal find warm up goals based on percentages

    : goal        : int   : final goal
    : percentages : tuple : the percents were to apply to the final goal
    : returns     : tuple : goals

    """
    return tuple([goal*p for p in percentages])
