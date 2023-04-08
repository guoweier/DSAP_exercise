# Design a circular positional list ADT that abstracts a circularly linked list in the same way that the positional list ADT abstracts a doubly linked list, with a notion of a designated "cursor" position within the list.

class _CircularLinkedList:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._cursor = self._Node(None,None)
        self._cursor._next = self._cursor
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_after(self, e, cursor):
        newest = self._Node(e, None)
        newest._next = cursor._next
        cursor._next = newest
        self._size += 1

    def _delete_after(self, cursor):
        node = cursor._next
        cursor._next = node._next
        self._size -= 1
        return node._element

class PositionalList(_CircularLinkedList):

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
        if node is self._cursor:
            return None
        else:
            return self.Position(self, node)

    # ----------------------- accessors ---------------------------- #
    def first(self):
        return self._make_position(self._cursor._next)

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
    def _insert_after(self, e, cursor):
        node = super()._insert_after(e, cursor)
        return self._make_position(node)

    def add_first_last(self, e):
        return self._insert_after(e, self._cursor)

    def add_before(self, p, e):
        c = p
        while c._next != p:
            c = c._next
        original = self._validate(c)
        return self._insert_after(e, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_after(e, original)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_after(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

if __name__ in "__main__":
    CL = PositionalList()
    for i in range(10):
        CL.add_first_last(i)
    print(list(CL))
