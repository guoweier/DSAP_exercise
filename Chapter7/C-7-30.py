# Exercise P-6-35 describes a LeakyStack abstraction. Implement that ADT using a singly linked list for storage.

# P-6-35:
# The Introduction of Section 6.1 notes that stacks are often used to provide "undo" support in applications like a Web browser or text editor. While support for undo can be implemented with an unbounded stack, many applications provide only limited support for such an undo history, with a fixed-capacity stack. When push is invoked with the stack at full capacity, a more typical semantic is to accept the pushed element at the top while "leaking" the oldest element from the bottom of the stack to make room. Give an implementation of such a LeakyStack abstraction, using a circular array with appropriate storage capacity. This class should have a public interface similar to the bounded-capacity stack in Exercise C-6-16, but with the desired leaky semantics when full.

class LinkedList:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, maxlen):
        self._cap = maxlen
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._cap

    def pop(self):
        if self.is_empty():
            raise ValueError("List is empty.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def push(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
            self._size += 1
        elif self.is_full():
            self._tail._next = newest
            self._head = self._head._next
        else:
            self._tail._next = newest
            self._size += 1
        self._tail = newest

    def top(self):
        if self.is_empty():
            raise ValueError("List is empty.")
        return self._head._element

if __name__ in "__main__":
    L = LinkedList(9)
    for i in range(10):
        L.push(i)
    print(L.top())
    for i in range(12):
        L.push(i)
    print(L.top())
