"""
Description
    Contains make goals which helps create the warm up sets

Functions
    * _make_goals
"""

def _make_goals(goal, percentages):
    """Form a final goal find warm up goals based on percentages"""
    return tuple([goal*p for p in percentages])
