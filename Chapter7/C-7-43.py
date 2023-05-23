# Describe a method for performing a card shuffle of a list of 2n elements, by converting it into two lists. A card shuffle is a permutation where a list L is cut into two lists, L1 and L2, where L1 is the first half of L and L2 is the second half of L, and then these two lists are merged into one by taking the first element in L1, then the first element in L2, followed by the second element in L1, the second element in L2, and so on.

# A base class providing a doubly linked list representation.
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
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e


def card_shuffle(L):
    # prepare L1 and L2
    L1 = PositionalList()
    L2 = PositionalList()
    num = len(L)
    # cut list L
    walk = L.first()
    for i in range(num//2):
        L1.add_last(walk.element())
        walk = L.after(walk)
    for j in range(num//2, num):
        L2.add_last(walk.element())
        walk = L.after(walk)
    # merge list
    Out = PositionalList()
    p1 = L1.first()
    p2 = L2.first()
    while p1 is not None:
        Out.add_last(p1.element())
        Out.add_last(p2.element())
        p1 = L1.after(p1)
        p2 = L2.after(p2)
    if len(L1) < len(L2):
        Out.add_last(p2.element())
    return Out

if __name__ in "__main__":
    L = PositionalList()
    for i in range(10):
        L.add_last(i+1)
    result = card_shuffle(L)
    cursor = result.first()
    while cursor is not None:
        print(cursor.element())
        cursor = result.after(cursor)
