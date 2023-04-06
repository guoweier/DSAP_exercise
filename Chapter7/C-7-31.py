# Design a forward list ADT that abstracts the operations on a singly linked list, much as the positional list ADT abstracts in the use of a doubly linked list. Implement a ForwardList class that supports such an ADT.

class _SinglyLinkedList:

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

    def is_empty():
        return self._size == 0

    def _insert_between(self, e, successor):
        newest = self._Node(e, successor)
        if self.is_empty():
            self._head = newest
        cursor = self._head
        if cursor == successor:
            newest._next = cursor
            self._head = newest
        else:
            while cursor._next != successor:
                cursor = cursor._next
            newest._next = cursor._next
            cursor._next = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        if self.is_empty():
            raise ValueError("List is empty.")
        if self.__len__() == 1:
            self._head = self._tail = None
        else:
            successor = node._next
            cursor = self._head
            if cursor == node:
                self._head = successor
            else:
                while cursor._next != node:
                    cursor = cursor._next
                cursor._next = successor
        self._size = 0
        element = node._element
        node._next = node._element = None
        return element


class ForwardList(_SinglyLinkedList):

    # --------------------- nested Position class ---------------------------- #
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not(self == other)

    # -------------------- utility method -------------------------- #
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type.")
        if p._container is not self:
            raise ValueError("p does not belong to this container.")
        if p._node._next is None:
            raise ValueError("p is no longer valid.")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # ----------------------- accessors ---------------------------- #
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------- mutators ------------------------------ #
    # override inherited version to return Position, rather than None
    def _insert_between(self, e, successor):
        node = super()._insert_between(e, successor)
        return self._make_position(node)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original)

    def add_after(self, p, e):
        original = self._validate(self, p._node._next)
        return self._insert_between(e, original)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

if __name__ in "__main__":
    FL = ForwardList()
