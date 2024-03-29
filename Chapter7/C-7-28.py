# Describe a fast recursive algorithm for reversing a singly linked list.

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
        if cursor._next == node:
            return cursor
        else:
            return self.get_cursor(node, cursor._next)

    def reverse(self, L, node = "end"):
        if node == "end":
            node = self._tail
            L.enqueue(node._element)

        cursor = self._head
        if node == self._head:
            L.enqueue(node._element)
            return L
        else:
            Cursor = self.get_cursor(node, cursor)
            L.enqueue(Cursor._element)
            node = Cursor
            return self.reverse(L, node)


if __name__ in "__main__":
    L = LinkedList()
    L2 = LinkedList()
    for i in range(20):
        L.enqueue(i)
    print(L.reverse(L2).first())
