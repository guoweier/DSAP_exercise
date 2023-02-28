# Describe a nonrecursive method for finding, by link hopping, the middle node of a doubly linked list with header and trailer sentinels. In the case of an even number of nodes, report the node slightly left of center as the "middle" (Note: This method must only use link hopping; it cannot use a counter.) What is the running time of this method.

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

    def middlenode(self):
        if self.is_empty():
            raise ValueError("Deque is empty.")
        node1 = self._header._next
        node2 = self._trailer._prev
        while node1 != node2 and node1._next != node2:
            node1 = node1._next
            node2 = node2._prev
        return node1._element

if __name__ in "__main__":
    D = LinkedDeque()
    for i in range(20):
        D.insert_first(i)
    print(D.middlenode())
