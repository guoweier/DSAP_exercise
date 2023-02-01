# Give a complete ArrayDeque implementation of the double-ended queue ADT as sketched in Section 6.3.2.

class ArrayDeque:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

if __name__ in "__main__":
    dq = ArrayDeque()
    for i in range(10):
        dq.add_last(i)
    dq.add_first(11)
    print(dq.first())
    print(dq.last())
