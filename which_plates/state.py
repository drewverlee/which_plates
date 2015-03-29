"""
Contains the State class
"""
from collections import Counter, namedtuple

Action = namedtuple("Action", ["action", "weights"])

class State:

    """ 
    State represents a state A* Search. It encapsulates a node in the graph
    and the action to reach that node.

    Its specific to the context of the problem, 
    in this case the search for the min wasted effort branch. 

    It contains meta information about the problem such as goals and 
    the path cost to reach this point.
    """

    def __init__(self, action, bar, plates, path_cost, goals, goal_i, parent):
        """
        action    : tuple : containing (""/"l"/"+"/"-", (weights,))
        path_cost : int    : the cost of this branch (all parent states up to the root)
        parent    : State  : the parent State
        goals     : tuple  : the goals of the problem, in this case, weight to lift
        bar       : list   : the weights currently on the bar, top is last/-1
        plates    : counter: the number of available plates
        goal_i    : int    : the current index of our goal
        """
        self.plates = plates
        self.action = action
        self.bar = sorted(bar)
        self.path_cost = path_cost
        self.goals = goals
        self.goal_i = goal_i
        self.parent = parent
        
        self.goal = self.goals[goal_i]

    def __repr__(self):
        return "{0}, {1}, {2}".format(self.node(), self.action, self.path_cost)

    def __str__(self):
        return "\nnode: {0}\naction: {1}\npath_cost: {2}".\
            format(self.node(), self.action, self.path_cost)

    def node(self):
        """a node in the graph"""
        return tuple(self.bar), self.goal_i

    def at_final_goal(self):
        """check if were at our final goal"""
        # recall that we add 0 to the end of the goals
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


        if not children:
            weights_removed = []
            for weight in reversed(self.bar):
                weights_removed.append(weight)
                children.append(self.remove_child(weights_removed))


        return children if children else [self.remove_child()]
                
    def lift_child(self):
        """create a child that represents the lift plates state"""
        action    = Action("l", self.bar)
        bar       = self.bar.copy()
        plates    = self.plates.copy()
        edge_cost = 0
        goal_i    = self.goal_i + 1
        path_cost = self.path_cost + edge_cost if self.parent else edge_cost
        parent    = self

        return State(action, bar, plates, path_cost, self.goals, goal_i, parent) 
        
    def add_child(self, weight):
        """create a child that represents the add plates state"""
        action    = Action("+", [weight])
        bar       = self.bar + [weight]
        plates    = self.plates.copy()
        edge_cost = 0
        goal_i    = self.goal_i
        path_cost = self.path_cost + edge_cost if self.parent else edge_cost
        parent    = self

        plates.subtract({weight: 1})

        return State(action, bar, plates, path_cost, self.goals, goal_i, parent) 


    def remove_child(self, weights_removed):
        """create a child that represents the remove plates state"""
        action    = Action('-', weights_removed)
        bar       = self.bar[:-len(weights_removed)]
        plates    = self.plates.copy()
        edge_cost = sum(weights_removed)
        goal_i    = self.goal_i
        path_cost = self.path_cost + edge_cost if self.parent else edge_cost
        parent    = self
        
        for weight in weights_removed:
            plates.update({weight: 1})

        return State(action, bar, plates, path_cost, self.goals, goal_i, parent) 

            
