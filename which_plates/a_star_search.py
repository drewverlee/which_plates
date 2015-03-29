"""
* a_star_search is a path finding algorithm thats used to discover the path
  minimizes wasted effort. Specifically, it finds the leaf node of the branch
  of least weight lifted.
"""


def a_star_search(state, fringe):
    visted = set()
    while fringe:
        state = fringe.deque()
        if state.at_final_goal():
            return state
        if state.node not in visited:
            visted.add(state.node)
            for child in state.children():
                fringe.enqueue(child)

