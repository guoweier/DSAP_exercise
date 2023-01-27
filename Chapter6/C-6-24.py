# Describe how to implement the stack ADT using a single queue as an instance variable, and only constant additional local memory within the metod bodies. What is the running time of the push(), pop(), and top() methods for your design?

class StackQueue:

    def __init__(self, q = []):
        self._stack = q

    def __len__(self):
        return len(self._stack)

    def is_empty(self):
        return len(self._stack)==0

    def push(self, val):
        size = len(self._stack)
        self._stack.append(val)
        for i in range(size):
            x = self._stack.pop(0)
            self._stack.append(x)

        return self._stack

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._stack.pop(0)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._stack[0]

if __name__ in "__main__":
    a = StackQueue()
    a.push(1)
    a.push(2)
    print(a.top())
    a.push(3)
    a.push(4)
    print(a.top())
    a.pop()
    print(a.top())

# push(): O(N)
# top(): O(1)
# pop(): O(1)
