# Our CircularQueue class of Section 7.2.2 provides a rotate() method that has semantics equivalent to Q.enqueue(Q.dequeue(), for a nonempty queue. Implement such a method for the LinkedQeueu calss of Section 7.1.2 without the creation of any new node.

class LinkedQueue:

    class _Node:
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

    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

def rotate(Q):
    if Q.__len__() > 1:
        x = Q.dequeue()
        Q.enqueue(x)


if __name__ in "__main__":
    Q = LinkedQueue()
    for i in range(10):
        Q.enqueue(i)
    for i in range(3):
        rotate(Q)
    print(Q.first())
