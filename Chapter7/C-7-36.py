# Give a complete implementation of the positional list ADT using a doubly linked list that does not include any sentinel nodes.

class _DoublyLinkedBase:

    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_before(self, e, successor):
        if self.is_empty():
            newest = self._Node(e, None, None)
            self._head = newest
            self._tail = newest
        elif successor == self._head:
            newest = self._Node(e, None, successor)
            self._head = newest
            successor._prev = newest
        else:
            predecessor = successor._prev
            newest = self._Node(e, predecessor, successor)
            predecessor._next = newest
            successor._prev = newest
        self._size += 1
        return newest

    def _insert_after(self, e, predecessor):
        if self.is_empty():
            newest = self._Node(e, None, None)
            self._head = newest
            self._tail = newest
        elif predecessor == self._tail:
            newest = self._Node(e, predecessor, None)
            self._tail = newest
            predecessor._next = newest
        else:
            successor = predecessor._next
            newest = self._Node(e, predecessor, successor)
            predecessor._next = newest
            successor._prev = newest
        self._size += 1
        return newest

    def _delete_before(self, node):
        if self.is_empty():
            raise ValueError("The list is empty.")
        elif self.__len__() == 1:
            self._head = None
            self._tail = None
        else:
            if node == self._head:
                self._head = node._next
            elif node == self._tail:
                self._tail = node._prev
            else:
                predecessor = node._prev
                successor = node._next
                predecessor._next = successor
                successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def _delete_after(self, node):
        if self.is_empty():
            raise ValueError("The list is empty.")
        elif self.__len__() == 1:
            self._head = None
            self._tail = None
        else:
            if node == self._tail:
                self._tail = predecessor
            elif node == self._head:
                self._head = node._next
            else:
                predecessor = node._prev
                successor = node._next
                predecessor._next = successor
                successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


# A sequential container of elements allowing positional access.
class PositionalList(_DoublyLinkedBase):

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
        if p._node is None:
            raise ValueError("p is no longer valid.")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node)

    # ----------------------- accessors ---------------------------- #
    def first(self):
        return self._make_position(self._head)

    def last(self):
        return self._make_position(self._tail)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor != self._tail:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------- mutators ------------------------------ #
    # override inherited version to return Position, rather than None
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_before(e, self._head)

    def add_last(self, e):
        return self._insert_after(e, self._tail)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_before(e, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_after(e, original)

    def delete_before(self, p):
        original = self._validate(p)
        return self._delete_before(original)

    def delete_after(self, p):
        original = self._validate(p)
        return self._delete_after(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

if __name__ in "__main__":
    L = PositionalList()
    for i in range(10):
        L.add_last(i)
    for j in range(4):
        L.delete_after(L.first())
    print(L.first().element())
