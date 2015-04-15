"""
Description
    Contains the State class and its supporting classes that help to build
    the graph in A*Search.

Classes
    * _State    : A node in the graph and the action to reach it.
    * _Action   : namedtuple.
    * _Priority : namedtuple.
    * _Node     : namedtuple.
"""
from collections import namedtuple


_Action = namedtuple("_Action", ["move", "weights"])
_Priority = namedtuple("_Priority", ["f_score", "used", "goal_i"])
_Node = namedtuple("_Node", ["bar", "goal_i"])


class _State:

    """
    _State represents a state in A* Search. It encapsulates a node in the graph
    and the action to reach that node, as well as some meta data about the
    problem such as the plates, goals, and path costs.
    """

    def __init__(self, action, bar, plates, path_cost, path_used, goals, goal_i, parent):
        """
        action    : tuple  : of the format (""/"l"/"+"/"-", (weights,))
        bar       : list   : the weights currently on the bar, top is last/-1
        plates    : counter: the number of available plates.
        path_cost : int    : the cost of this branch.
        path_used : int    : total number of plates used/moved in this branch.
        parent    : _State  : the parent _State.
        goals     : tuple  : the weights we want to lift.
        goal_i    : int    : the current index of our goal
        """
        self.plates    = plates
        self.action    = action
        self.bar       = bar
        self.path_cost = path_cost
        self.path_used = path_used
        self.goals     = goals
        self.goal_i    = goal_i
        self.parent    = parent

        # convince attribute
        self.goal = self.goals[goal_i]

    def __repr__(self):
        return """
            {action},
            {bar},
            {plates},
            {path_cost},
            {path_used},
            {goal},
            {goal_i},
            {goals},
            {g_score},
            {h_score},
            {f_score},
            """.format(
                action    = self.action,
                bar       = self.bar,
                plates    = self.plates,
                path_cost = self.path_cost,
                path_used = self.path_used,
                goal      = self.goal,
                goal_i    = self.goal_i,
                goals     = self.goals,
                g_score   = self._g_score(),
                h_score   = self._h_score(),
                f_score   = self._f_score()
            )

    def __str__(self):
        return """
            ============= * STATE * =============
            action    : {action}
            bar       : {bar}
            plates    : {plates}

            path cost : {path_cost}
            path used : {path_used}

            goal      : {goal}
            goal_i    : {goal_i}
            goals     : {goals}

            g score   : {g_score}
            h score   : {h_score}
            f score   : {f_score}
            """.format(
                action    = self.action,
                bar       = self.bar,
                plates    = self.plates,

                path_cost = self.path_cost,
                path_used = self.path_used,

                goal      = self.goal,
                goal_i    = self.goal_i,
                goals     = self.goals,

                g_score   = self._g_score(),
                h_score   = self._h_score(),
                f_score   = self._f_score()
            )

    def __lt__(self, other):
        return self._f_score() < other._f_score()

    @classmethod
    def make_start_state(cls, goals, plates):
        """Creates the start state.

        Arguments
            goals  : tuple   : the weights we want to lift.
            plates : Counter : plates we have to use.

        Returns
            start state : state :
        """
        action    = _Action("", [])
        bar       = []
        path_cost = 0
        path_used = 0
        goal_i    = 0
        parent    = None
        goals     = goals + (0,)
        return _State(action, bar, plates, path_cost, path_used, goals, goal_i,
            parent)

    def priority(self):
        """Return priority of the state

        Description
            the priority highest priority is the lowest number so
            (1, 2, 3) has a higher priority then (2, 0, 0)
        """
        return _Priority(self._f_score(), self.path_used, -self.goal_i)

    def _f_score(self):
        """Return the f score."""
        return self._g_score() + self._h_score()

    def _g_score(self):
        """Return the g score

        Description
            In general the g score is a measure of total cost to reach a
            point.

            In our problem, the its the cost of any weights we have
            to remove from the bar.
        """
        return self.path_cost

    def _h_score(self):
        """Return the h score.

        Description
            In general h score is measure of the estimated cost to our goal.
            In order to be consistent (and so allow A*Search to always find
            the optimal goal) it can never over estimate the cost.

            In our problem the H score is the different between the current
            weight on the bar and the current goal weight. Except in the
            start state "" and lift states "l", which are just their
            to make the solutions easier to read.
        """
        if self.action.move == '+' or self.action.move == '-':
            return self.goal - sum(self.bar)
        elif self.action.move == '' or self.action.move == 'l':
            return 0

    def node(self):
        """Returns states node representation"""
        return _Node(tuple(self.bar), self.goal_i)

    def at_final_goal(self):
        """Check if were at our final goal"""
        # NOTE: 0 is added to the every goals list to avoid indexing errors
        return self.goal_i == len(self.goals) - 1

    def children(self):
        """Create children of state

        Their are 3 actions possible to create a child state and so
        their are 3 different methods to create children called from
        within children:

        l = lift means we move to the next goal
        + = add plate.
        - = remove plates

        It will create children that are consistent, that is, states with
            estimated f scores less then the actual f score. But will also
            create children we know wont be expanded due to the closed set
        """
        if sum(self.bar) == self.goal:
            return [self._lift_child()]

        children = []

        for weight, quantity in self.plates.items():
            if quantity > 0 and sum(self.bar) + weight <= self.goal:
                children.append(self._add_child(weight))

        current_state = self
        if not children:
            while current_state.action.move != 'l' and current_state.parent != None:
                current_state = current_state.parent

            weights_removed = []
            for weight in reversed(current_state.bar):
                weights_removed.append(weight)
                children.append(current_state._remove_child(current_state,
                    weights_removed.copy()))

        return children

    def _lift_child(self):
        """Create a child that represents the lift plates state."""
        bar       = self.bar.copy()
        action    = _Action("l", bar)
        plates    = self.plates.copy()
        edge_cost = 0
        goal_i    = self.goal_i + 1
        path_cost = self.path_cost + edge_cost if self.parent else edge_cost
        path_used = self.path_used + 0
        parent    = self

        return _State(action, bar, plates, path_cost, path_used, self.goals,
            goal_i, parent)

    def _add_child(self, weight):
        """Create a child that represents the add plates state."""
        bar       = self.bar + [weight]
        action    = _Action("+", [weight])
        plates    = self.plates.copy()
        edge_cost = 0
        goal_i    = self.goal_i
        path_cost = self.path_cost + edge_cost if self.parent else edge_cost
        path_used = self.path_used + 1
        parent    = self

        plates.subtract({weight: 1})

        return _State(action, bar, plates, path_cost, path_used, self.goals,
            goal_i, parent)

    def _remove_child(self, parent_state, weights_removed):
        """Create a child that represents the remove plates state."""
        bar       = parent_state.bar[:-len(weights_removed)]
        action    = _Action('-', weights_removed)
        plates    = parent_state.plates.copy()
        edge_cost = sum(weights_removed)
        goal_i    = parent_state.goal_i
        path_cost = parent_state.path_cost + edge_cost if parent_state.parent else edge_cost
        path_used = parent_state.path_used + len(weights_removed)
        parent    = parent_state

        for weight in weights_removed:
            plates.update({weight: 1})

        return _State(action, bar, plates, path_cost, path_used,
            parent_state.goals, goal_i, parent)

    def path(self):
        """Returns the path of actions leading to this state."""
        path          = []
        current_state = self
        roots_parent  = None

        while current_state != roots_parent:
            path.append(current_state.action)
            current_state = current_state.parent

        # reversed so we can read start to finish.
        path.reverse()

        return path
