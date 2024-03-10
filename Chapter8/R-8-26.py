# The collections.deque class supports an extend method that adds a collection of elements to the end of the queue at once. Reimplement the breadthfirst method of the Tree class to take advantage of this feature.

from collections import deque

def breadthfirst(self):
    # Generate a breadth-first iteration of the positions of the tree.
    if not self.is_empty():
        fringe = deque()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p
            fringe.extend(self.children(p)) 
