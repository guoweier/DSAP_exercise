# In certain applications of the queue ADT, it is common to repeatedly dequeue an element, process it in some way, and then immediately enqueue the same element. Modify the ArrayQueue implementation to include a rotate() method that has semantics identical to the combination, Q.enqueue(Q.dequeue()). However, your implementation should be more efficient than making two separate callls (for example, because there is no need to modify _size).

class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        slef._front = 0

    def rotate(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        x = self._data[self._front]
        self._data[self._front] = None
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = x
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)

if __name__ in "__main__":
    q = ArrayQueue()
    for i in range(10):
        q.enqueue(i)
    q.rotate()
    print(q.first())
