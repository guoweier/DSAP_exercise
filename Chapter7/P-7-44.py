# Write a simple text editor that stores and displays a string of characeters using the positional list ADT, together with a cursor object that highlights a position in this string. A simple interface is to print the string and then to use a second line of output to underline the position of the cursor. Your editor should support the following operations:
# - left: Move cursor left one character (do nothing if at beginning)
# - right: Move cursor right one character (do nothing if at end)
# - insert c: Insert the character c just after the cursor.
# - delete: Delete the character just after the cursor (do nothing at end)

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

class TextEditor:

    def __init__(self, string):
        self._text = PositionalList()
        for char in string:
            self._text.add_last(char)
        self._cursor = self._text.first()

    def _print_string(self):
        line = ""
        p = self._text.first()
        while p is not None:
            line += p.element()
            p = self._text.after(p)
        return line

    def _print_cursor(self, direction):
        line = ""
        walk = self._text.first()
        n = 0
        while walk != self._cursor:
            walk = self._text.after(walk)
            n += 1
        if direction == "left":
            for i in range(n-1):
                line += " "
        elif direction == "right":
            for i in range(n+1):
                line += " "
        line += "_"
        return line

    def left(self):
        line1 = self._print_string()
        if self._cursor == self._text.first():
            line2 = "_"
        else:
            line2 = self._print_cursor("left")
        print(line1+"\n"+line2)

    def right(self):
        line1 = self._print_string()
        if self._cursor == self._text.last():
            line2 = ""
            str_len = len(self._text)
            for i in range(str_len-1):
                line2 += " "
            line2 += "_"
        else:
            line2 = self._print_cursor("right")
        print(line1+"\n"+line2)

    def insert(self, c):
        
