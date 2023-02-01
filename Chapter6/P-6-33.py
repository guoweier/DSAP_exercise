# Give an array-based implementation of a double-ended queue supporting all of the public behaviors shown in Table 6.4 for the collection.deque class, including use of the maxlen optional parameter. When a length-limited deque is full, provide semantics similar to the collections.deque class, whereby a call to insert an element on one end of a deque causes an element to be lost from the opposite side.

class CollectionDeque:

    def __init__(self, maxlen):
        self._maxlen = maxlen
        self._data = [None]*self._maxlen
        self._size = 0
        self._front = 0

    
