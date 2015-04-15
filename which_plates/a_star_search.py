"""
Functions:
    _a_star_search: a searching algorithm for finding the final state along
    the optimal path.
"""


def _a_star_search(root, Que):
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
        Given a Que containing the start_state with goals 20, 25, 0 and plates
            20 and 25 the following search would unfold...

            State  action   bar   goal 
            0      '',[]    []    0
            1      +, [20]  [20]  0
            2      l, [20]  [20]  1
            3      -, [20]  []    1
            4      +, [25]  [25]  1
            5      l, [25]  [25]  2

        With State '5' being the returned final state.

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
