"""
contains PriorityQue class
"""

import heapq


class PriorityQue(list):
    
    """ PriorityQue adds and removes items based on the provided priority """

    def __init__(self, items):
        for item in items:
            self.enqueue(item)

    def enqueue(self, item):
        """add item
        
        item should have a priority method
        """
        heapq.heappush(self, (item.priority(), item))

    def deque(self):
        """remove and return item with highest priority"""
        return heapq.heappop(self)[1]
