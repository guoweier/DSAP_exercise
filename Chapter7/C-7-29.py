# Describe in detail an algorithm for reversing a singly linked list L using only a constant amount of additional space and not using any recursions.

class LinkedList:

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
            raise ValueError("List is empty.")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise ValueError("List is empty.")
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

    def get_cursor(self, node, cursor):
        while cursor._next != node:
            cursor = cursor._next
        return cursor

    def reverse(self, L):
        if L.is_empty():
            L.enqueue(self._tail._element)
            node = self._tail

        cursor = self._head
        while node != self._head:
            Cursor = self.get_cursor(node, cursor)
            L.enqueue(Cursor._element)
            node = Cursor
        L.enqueue(self._head._element)
        return L

if __name__ in "__main__":
    L = LinkedList()
    L2 = LinkedList()
    for i in range(20):
        L.enqueue(i)
    print(L.reverse(L2).first())
