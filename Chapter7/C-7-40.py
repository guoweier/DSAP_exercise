# Describe an efficient method for maintaining a favorites list L, with move-to-front heuristic, such that elements that have not been accessed in the recent n accesses are automatically purged from the list.

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

# List of elements ordered from most frequently accessed to least.
class FavoritesList:

    # -------------------------------- nested _Item class ------------------------------------ #
    class _Item:
        __slots__ = '_value', '_count', '_access'
        def __init__(self,e):
            self._value = e
            self._count = 0
            self._access = 0

    # ------------------------------ nonpublic utilities ----------------------------- #
    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    # ------------------------------ public methods ---------------------------------- #
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        p = self._find_position(e)
        Op = self._data.first()
        if p is None:
            p = self._data.add_last(self._Item(e))
        while Op is not None:
            if Op != p:
                Op.element()._access += 1
            Op = self._data.after(Op)
        p.element()._count += 1
        p.element()._access = 0
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p != self._data.last():
            en = self._data.after(p).element()._value
            self._data.delete(p)
            return en
        else:
            self._data.delete(p)
            return None

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k.")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)


# List of elements ordered with move-to-front heuristic
class FavoritesListMTF(FavoritesList):

    # override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    # override top because list is no longer sorted
    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k.")
        # we begin making a copy of the original list
        temp = PostionalList()
        for item in self._data:
            temp.add_last(item)

        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found the element with highest count
            yield highPos.element()._value
            temp.delete(highPos)

    def purge(self, n):
        p = self._data.first()
        Out = FavoritesListMTF()
        while p.element()._access < n:
            Out.access(p)
            p = self._data.after(p)


if __name__ in "__main__":
    FL = FavoritesListMTF()
    for i in range(10):
        FL.access(i)
    for j in range(5):
        FL.access(j)
    for k in range(4):
        FL.access(k)
    FL.access(6)
    FL.purge(5)
    print(FL.top(4))
