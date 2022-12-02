# Modify the ArrayStack implementation so that the stack's capacity is limited to maxlen elements, where maxlen is an optional parameter to the constructor (that defualts to None). If push is called when the stack is at full capacity, throw a Full exception (defined similarly to Empty).

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self,maxlen):
        "Creat an empty stack."
        self._data = []
        self._maxlen = maxlen

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
            raise ValueError('Stack is full.')
        return self._data.append(e)

    def top(self):
        """Return (but not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise ValueError('Stack is empty.')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise ValueError('Stack is empty.')
        return self._data.pop()

if __name__ in '__main__':
    a = ArrayStack(3)
    for i in range(3):
        a.push(i)
    print(a)
    print(a.push(4))
