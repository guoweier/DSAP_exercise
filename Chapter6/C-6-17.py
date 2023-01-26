# In the previous excercise, we assume that the underlying list is initially empty. Redo that exercise, this time preallocating an underlying list with length equal to the stack's maximum capacity.

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self,maxlen):
        "Creat an empty stack."
        self._maxlen = maxlen
        self._data = [None]*self._maxlen

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) == self._maxlen

    def push(self,e):
        """Add element e to the top of the stack.
        Raise Full exception if the stack is full.
        """
        if self.is_full():
            raise Empty('Stack is full')
        return self._data.append(e)

    def top(self):
        """Return (but not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is full.')
        return self._data.pop()
