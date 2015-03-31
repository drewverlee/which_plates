"""
Functions:
    a_star_search: a searching algorithm that.
"""


def a_star_search(root, Que):
    """Returns the final/leaf state.

    Description
        a path finding algorithm thats used to discover the
        path that minimizes wasted effort.

        In the context of our problem, it finds the leaf node
        of the branch of least weight lifted.

        To find the final state, A star search my carefully create the
        search tree, making sure that it only creates expands nodes (creates
        new edges towards the goal) once per node. This is achieved by
        pruning away nodes we have 'visited' before.

    Example
        see tests/test_plates_10_10_15_20_w_goals_20_25_40.py and conftest.py
            for a convincing example.

    Arguments
        root  : State : root state
        Que   : Que   : any enqueue and deque states based on priority

    Returns
        final state : State : the state which achieves the final goal.
    """
    fringe = Que([root])
    visited = set(root.node())

    while fringe:
        state = fringe.deque()
        if state.at_final_goal():
            return state
        for child in state.children():
            if child.node() not in visited:
                visited.add(child.node())
                fringe.enqueue(child)
