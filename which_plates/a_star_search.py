"""
* a_star_search is a path finding algorithm thats used to discover the path
  minimizes wasted effort. Specifically, it finds the leaf node of the branch
  of least weight lifted.
"""


def a_star_search(root, Que):
    """return final state
    root : state: root state
    Que  : que   : that can add and remove states based on priority
    rtype : State : final state
    """
    fringe = Que([root])
    visited = set()

    while fringe:
        state = fringe.deque()
        if state.at_final_goal():
            return state
        if state.node not in visited:
            visited.add(state.node)
            for child in state.children():
                fringe.enqueue(child)
