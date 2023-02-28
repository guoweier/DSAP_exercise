# Give a fast algorithm for concatenating two doubly linked lists L amd M, with header and trailer sentinel nodes, into a single last L'.

class _DoublyLinkedBase:

    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise ValueError("Deque is empty.")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise ValueError("Deque is empty.")
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Deque is empty.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise ValueError("Deque is empty.")
        return self._delete_node(self._trailer._prev)

    def concatlist(self, M):
        node = M._header._next
        while node != M._trailer:
            self.insert_last(node._element)
            node = node._next
        return self

if __name__ in "__main__":
    L = LinkedDeque()
    M = LinkedDeque()
    for i in range(20):
        L.insert_last(i)
        M.insert_last(i+10)
    newL = L.concatlist(M)
    print(newL.last())
