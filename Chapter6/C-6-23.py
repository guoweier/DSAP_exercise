# Suppose you have three nonempty stacks R, S, and T. Describe s sequence of operations taht results in S storing all elements originally in T below all of S's original elements, with both sets of those elements in their original order. The final configuration for R should be the same as its original configuration. For example, if R = [1,2,3], S = [4,5], T = [6,7,8,9], the final configuration should have R = [1,2,3] and S = [6,7,8,9,4,5]


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, list=[]):
        "Creat an empty stack."
        self._data = list

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0


    def push(self,e):
        """Add element e to the top of the stack.
        """
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

    def to_list(self):
        self._list = [item for item in self._data]
        return self._list



def combine_stack(R,S,T):
    # temporarily store all T elements in R (for oppositing order)
    nT = len(T)
    for i in range(nT):
        R.push(T.pop())
    # move all S elements to T
    for i in range(len(S)):
        T.push(S.pop())
    # move original T elements into S
    for i in range(nT):
        S.push(R.pop())
    # move original S elements back into S
    for i in range(len(T)):
        S.push(T.pop())

    return [R.to_list(), S.to_list()]

if __name__ in "__main__":
    R = ArrayStack([1,2,3])
    S = ArrayStack([4,5])
    T = ArrayStack([6,7,8,9])
    print(combine_stack(R,S,T))
