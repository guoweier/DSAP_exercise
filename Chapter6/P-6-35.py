# The Introduction of Section 6.1 notes that stacks are often used to provide "undo" support in applications like a Web browser or text editor. While support for undo can be implemented whith an unbounded stack, many applications provide only limited support for such an undo history, with a fixed-capacity stack. When push is invoked with the stack at full capacity, a more typical semantic is to accept the pushed element at the top while "leaking" the oldest element from the bottom of the stack to make room. Give an implementation of such a LeakyStack abstraction, using a circular array with appropriate storage capacity. This class should have a public interface similar to the bounded-capacity stack in Exercise C-6-16, but with the desired leaky semantics when full.

class LeakyStack:

    def __init__(self, maxlen):
        self._cap = maxlen
        self._data = [None]*self._cap
        self._size = 0
        self._front = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._cap

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty.")
        back = (self._front+self._size-1) % self._cap
        self._size -= 1
        return self._data.pop(back)

    def push(self, e):
        if self.is_full():
            self._data[self._front] = e
            self._front = (self._front+1) % self._cap
        else:
            self._data.append(e)
            self._size += 1

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty.')
        back = (self._front+self._size-1) % self._cap
        return self._data[back]

if __name__ in "__main__":
    LS = LeakyStack(9)
    for i in range(10):
        LS.push(i)
    print(LS.top())
    LS.push(11)
    print(LS.top())
