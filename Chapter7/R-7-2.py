# Descrobe a good algorithm for concatenating two singly linked lists L and M, given only references to the first node of each list, into a single list L' that contains all the nodes of L followed by all the nodes of M.

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

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def concatList(self, M):
        Lprime = []
        # add L elements into L'
        nodeL = self._head
        while nodeL._next != None:
            Lprime.append(nodeL._element)
            nodeL = nodeL._next
        Lprime.append(self._tail._element)
        # add M elements into L'
        nodeM = M._head
        while nodeM._next != None:
            Lprime.append(nodeM._element)
            nodeM = nodeM._next
        Lprime.append(M._tail._element)
        return Lprime

if __name__ in "__main__":
    L = LinkedQueue()
    M = LinkedQueue()
    for i in range(10):
        L.enqueue(i)
        M.enqueue(i+2)
    print(L.concatList(M))
