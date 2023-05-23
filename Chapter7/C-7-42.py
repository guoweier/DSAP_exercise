# Write a Scoreboard class that maintains the top 10 scores for a game application using a singly linked list, rather than the array that was used in Section 5.5.1.

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
        __slots__ = '_name', '_score'
        def __init__(self, name, score):
            self._name = name
            self._score = score

    # ------------------------------ nonpublic utilities ----------------------------- #
    def _find_position(self, name):
        walk = self._data.first()
        while walk is not None and walk.element()._name != name:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p != self._data.first():
            cnt = p.element()._score
            walk = self._data.before(p)
            if cnt > walk.element()._score:
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._score):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    # ------------------------------ public methods ---------------------------------- #
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, name, score):
        p = self._find_position(name)
        if p is None:
            p = self._data.add_last(self._Item(name, score))
        oldscore = p.element()._score
        if score > oldscore:
            p.element()._score = score
            self._move_up(p)

    def remove(self, name):
        p = self._find_position(name)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k.")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield '\t'.join([item._name, item._score])
            walk = self._data.after(walk)


# class for game scoreboard
class Scoreboard:

    def __init__(self):
        self._board = FavoritesList()

    def __len__(self):
        return len(self._board)

    def is_empty(self):
        return len(self._board) == 0

    def __getitem__(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k.")
        walk = self._board.first()
        for j in range(k-1):
            walk = self._board.after(walk)
        item = walk.element()
        return '\t'.join([item._name, item._score])

    def __str__(self):
        walk = self._board.first()
        if len(self) < 10:
            while walk is not None:
                item = walk.element()
                yield '\t'.join([item._name, item._score])
                walk = self._board.after(walk)
        else:
            for i in range(10):
                item = walk.element()
                yield '\t'.join([item._name, item._score])
                walk = self._board.after(walk)

    def add(self, name, score):
        newboard = self._board.access(name, score)
        newboard.__str__()

if __name__ in "__main__":
    SB = Scoreboard()
    player = ["Alice", "Bob", "Celina", "David", "Emily", "Frank", "Grace", "Henry", "Ivy", "Jason", "Kevin", "Lucy", "Mandy", "Nancy", "Olive", "Peter", "Quinlan", "Robin", "Sam", "Tommy", "Umar", "Vicky", "Wendy", "Xavier", "Yara", "Zack"]
    for i in range(len(player)):
        SB.add(player[i], i+1)
    SB.add("David", 56)
    SB.add("Sam", 93)
    SB.add("Olive", 39)
    SB.add("Umar", 83)
    SB.add("Nancy", 75)
    SB.__str__()
