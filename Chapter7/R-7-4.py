# Describe in detail how to swap two nodes x and y (and not just their contents) in a singly linked list L given references only to x and y. Repeat thsi exercise for the case when L is a doubly linked list. Which algorithm takes more time?

from time import time

class SinglyLinkedList:

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

    def append(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def identify_node(self, e):
        node = self._head
        while node._element != e:
            node = node._next
        return node

    def singly_swap_nodes(self,x,y):
        node = self._head
        if node == x:
            self._head = y
            y._next = x
            x._next = y._next
        else:
            while node._next != x:
                node = node._next
            node._next = y
            y._next = x
            x._next = y._next

class DoublyLinkedList:

    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
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

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def identify_node(self,e):
        node = self._header._next
        while node._element != e:
            node = node._next
        return node

    def doubly_swap_nodes(self, x, y):
        predecessor = x._prev
        successor = y._next
        predecessor._next = y
        successor._prev = x
        y._prev = predecessor
        y._next = x
        x._prev = y
        x._next = successor

if __name__ in "__main__":
    S = SinglyLinkedList()
    D = DoublyLinkedList()
    for i in range(1000):
        S.append(i)
        D.insert_last(i)
    x1 = S.identify_node(880)
    y1 = S.identify_node(881)
    x2 = D.identify_node(880)
    y2 = D.identify_node(881)

    start_t1 = time()
    S.singly_swap_nodes(x1,y1)
    end_t1 = time()
    print(end_t1-start_t1)

    start_t2 = time()
    D.doubly_swap_nodes(x2,y2)
    end_t2 = time()
    print(end_t2-start_t2)
