# Although we have used a doubly linked list to implement the positional list ADT, it is possible to support the ADT with an array-based implementation. The key is to use the composition pattern and store a sequence of position items, where each item stores an element as well as that element's current index in the array. Whenever an element's place in the array is changed, the recorded index in the position must be updated to match. Given a complete class providing such an array-based implementation of the positional list ADT. What is the efficiency of the various operations?

import numpy as np

# A base class providing a doubly linked list representation.
class _ArrayBase:

    class _Node:
        def __init__(self, element, index):
            self._element = element
            self._index = index

    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _add(self, e, index):
        newest = self._Node(e, 0)
        self._data.append(newest)
        self._size += 1
        j = self._size - 2
        while index <= j:
            self._data[j]._index += 1
            self._data[j+1]._index -= 1
            self._data[j], self._data[j+1] = self._data[j+1], self._data[j]
            j -= 1
        return newest

    def _delete(self, node):
        delete_index = node._index
        delete_element = node._element
        if self._size == 1:
            self._data = []
        else:
            for j in range(delete_index, self._size):
                self._data[j+1]._index -= 1
                self._data[j]._index += 1
                self._data[j], self._data[j+1] = self._data[j+1], self._data[j]
            self._data.pop()
        self._size -= 1
        node._element = node._index = None
        return delete_element


# A sequential container of elements allowing positional access.
class PositionalList(_ArrayBase):

    # --------------------- nested Position class ---------------------------- #
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def index(self):
            return self._node._index

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
        if p._node._index is None:
            raise ValueError("p is no longer valid.")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node)

    # ----------------------- accessors ---------------------------- #
    def first(self):
        return self._make_position(self._data[0])

    def last(self):
        return self._make_position(self._data[self._size-1])

    def before(self, p):
        node = self._validate(p)
        node_index = node._index
        if node_index == 0:
            return ValueError("This is the first node of array. There is no node before.")
        else:
            return self._make_position(self._data[node_index-1])

    def after(self, p):
        node = self._validate(p)
        node_index = node._index
        if node_index == self._size - 1:
            return ValueError("This is the last node of array. There is no node after.")
        else:
            return self._make_position(self._data[node_index+1])

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------- mutators ------------------------------ #
    # override inherited version to return Position, rather than None
    def _add(self, e, index):
        node = super()._add(e, index)
        return self._make_position(node)

    def add_first(self, e):
        return self._add(e, 0)

    def add_last(self, e):
        return self._add(e, self._size)

    def add_before(self, p, e):
        original = self._validate(p)
        or_index = original._index
        return self._add(e, or_index-1)

    def add_after(self, p, e):
        original = self._validate(p)
        or_index = original._index
        return self._add(e, or_index+1)

    def delete(self, p):
        original = self._validate(p)
        return self._delete(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e

if __name__ in "__main__":
    L = PositionalList()
    for i in range(10):
        L.add_last(i)
    one = L.first()
    L.add_after(one, 15)
    L.replace(one, 14)
    two = L.after(one)
    print(L.first().element())
    print(L.after(two).element())
