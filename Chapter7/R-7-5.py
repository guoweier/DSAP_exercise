# Implement a function that counts the number of nodes in a circularly linked list.

class CircularQueue:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self,e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 1:
            self._tail = self._tail._next

    def countnode(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        node = self._tail
        num = 1
        while node._next != self._tail:
            num += 1
            node = node._next
        return num

if __name__ in "__main__":
    Q = CircularQueue()
    for i in range(20):
        Q.enqueue(i)
    print(Q.countnode())
