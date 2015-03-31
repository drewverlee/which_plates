"""
Description
    PriorityQue allows for simple interface for enqueue and deque any object
    that has a priority function.

Classes
    * PriorityQue: which extends list class.
"""

import heapq


class PriorityQue(list):

    """ PriorityQue adds and removes items based on the provided priority """

    def __init__(self, items):
        for item in items:
            self.enqueue(item)

    def enqueue(self, item):
        """Add item to the que"""
        heapq.heappush(self, (item.priority(), item))

    def deque(self):
        """remove and return item with highest priority"""
        return heapq.heappop(self)[1]
