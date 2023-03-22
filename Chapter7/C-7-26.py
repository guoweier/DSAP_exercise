# Implement a method, concatenate(Q2) for the LinkedQueue class that takes all elements of LinkedQueue Q2 and appends them to the end of the original queue. The operation should run in Q(1) time and should result in Q2 being an empty queue.

class LinkedQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def concatenate(self, Q2):
        if self.is_empty():
            self._head = Q2._head
        else:
            self._tail._next = Q2._head
        self._size += Q2.__len__()
        Q2._head = None
        Q2._tail = None
        Q2._size = 0

if __name__ in "__main__":
    Q1 = LinkedQueue()
    for i in range(10):
        Q1.enqueue(i+1)
    Q2 = LinkedQueue()
    for j in range(5):
        Q2.enqueue(j)
    Q1.concatenate(Q2)
    for i in range(len(Q1)):
        print(Q1.dequeue())
