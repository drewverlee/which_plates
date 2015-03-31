"""
Contains: 

* the State class
* Action namedtuple
* Priority namedtuple
"""
from collections import Counter, namedtuple

Action = namedtuple("Action", ["move", "weights"])
Priority = namedtuple("Priority", ["f_score", "goal_i", "used"])
Node = namedtuple("Node", ["bar", "goal_i"])

class State:

    """ 
    State represents a state A* Search. It encapsulates a node in the graph
    and the action to reach that node.

    Its specific to the context of the problem, 
    in this case the search for the min wasted effort branch. Which, because,
    we always choose the heavier plates first is
    also the branch that minimizes the amount of plates used.

    It contains meta information about the problem such as goals and 
    the path cost to reach this point.
    """

    def __init__(self, action, bar, plates, path_cost, path_used, goals, goal_i, parent):
        """
        action    : tuple : containing (""/"l"/"+"/"-", (weights,))
        bar       : list   : the weights currently on the bar, top is last/-1
        plates    : counter: the number of available plates
        path_cost : int    : the cost of this branch (all parent states up to the root)
        path_used : int    : total number of plates used of this branch
        parent    : State  : the parent State
        goals     : tuple  : the goals of the problem, in this case, weight to lift


        goal_i    : int    : the current index of our goal
        """
        self.plates = plates
        self.action = action
        self.bar = bar
        self.path_cost = path_cost
        self.path_used = path_used
        self.goals = goals
        self.goal_i = goal_i
        self.parent = parent
        
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
                    g_score   = self.g_score(),
                    h_score   = self.h_score(),
                    f_score   = self.f_score()
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

                    g_score   = self.g_score(),
                    h_score   = self.h_score(),
                    f_score   = self.f_score()
                )

    # TODO, i don't think i should need this once priority is corrent,
    # it indicates a tie that i didn't explicit break
    def __lt__(self, other):
        return self.f_score() < other.f_score()


    # CLASS METHOD TODO is there a decorator or something?
    def make_start_state(goals, plates):
        """returns the start state

        :goals: tuple:  goals of the lift
        :plates: Counter: plates we have to use
        :returns: State: the start state
        """
        action    = Action("", [])
        bar       = []
        path_cost = 0
        path_used = 0
        goal_i    = 0
        parent    = None
        goals     = goals + (0,) #NOTE to be constant make children, maybe goals should be a list
        return State(action, bar, plates, path_cost, path_used, goals, goal_i, parent)

    # INSTANTS METHOD
    def priority(self):
        """return priority of the state
        
        the priority highest priority is the lowest number
        """
        return Priority(self.f_score(), self.path_used, len(self.goals) - self.goal_i)

    def f_score(self):
        """return the f score"""
        return self.g_score() + self.h_score()

    def g_score(self):
        """return the g score"""
        return self.path_cost

    def h_score(self):
        """return the h score
       
        the lift state is free
        """
        #TODO fix this... 
        move = self.action.move
        return self.goal - sum(self.bar) if (move == '+' or move == "-") else 0

    def node(self):
        """a node in the graph"""
        return Node(tuple(self.bar), self.goal_i)

    def at_final_goal(self):
        """check if were at our final goal"""
        # NOTE: 0 is added to the every goals list to avoid index errors
        return self.goal_i == len(self.goals) - 1

    def children(self):
        """create children of state

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
            return [self.lift_child()]

        children = []
        
        for weight, quantity in self.plates.items():
            if quantity > 0 and sum(self.bar) + weight <= self.goal:
                children.append(self.add_child(weight))

        current_state = self
        if not children:
            while current_state.action.move != 'l' and current_state.parent != None:
                current_state = current_state.parent

            weights_removed = []
            for weight in reversed(current_state.bar):
                weights_removed.append(weight)
                children.append(current_state.remove_child(current_state, weights_removed.copy()))

        return children

    def lift_child(self):
        """create a child that represents the lift plates state"""
        bar       = self.bar.copy()
        action    = Action("l", bar)
        plates    = self.plates.copy()
        edge_cost = 0
        goal_i    = self.goal_i + 1
        path_cost = self.path_cost + edge_cost if self.parent else edge_cost
        path_used = self.path_used + 0
        parent    = self

        return State(action, bar, plates, path_cost, path_used, self.goals, goal_i, parent) 

    def add_child(self, weight):
        """create a child that represents the add plates state"""
        bar       = self.bar + [weight]
        action    = Action("+", [weight])
        plates    = self.plates.copy()
        edge_cost = 0
        goal_i    = self.goal_i
        path_cost = self.path_cost + edge_cost if self.parent else edge_cost
        path_used = self.path_used + 1
        parent    = self

        plates.subtract({weight: 1})

        return State(action, bar, plates, path_cost, path_used, self.goals, goal_i, parent) 

    def remove_child(self, pstate, weights_removed):
        """create a child that represents the remove plates state"""
        bar       = pstate.bar[:-len(weights_removed)]
        action    = Action('-', weights_removed)
        plates    = pstate.plates.copy()
        edge_cost = sum(weights_removed)
        goal_i    = pstate.goal_i
        path_cost = pstate.path_cost + edge_cost if pstate.parent else edge_cost
        path_used = pstate.path_used + len(weights_removed)
        parent    = pstate
        
        for weight in weights_removed:
            plates.update({weight: 1})

        return State(action, bar, plates, path_cost, path_used, pstate.goals, goal_i, parent) 

    def path(self):
        """returns the path of actions leading to this state

        
        :returns: list: of (action, [plates])

        """
        path          = []
        current_state = self
        roots_parent  = None

        while current_state != roots_parent:
            path.append(current_state.action)
            current_state = current_state.parent

        path.reverse()

        return path


        
        


