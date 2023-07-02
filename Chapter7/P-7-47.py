# Implement a CardHand class that supports a person arranging a group of cards in his or her hand. The simulator should reperesent the sequence of cards using a single positional list ADT so that cards of the same suit are kept together. Implement this strategy by means of four "fingers" into the hand, one for each of the suits of hearts, clubs, spades, and diamonds, so that adding a new card to the person's hand or playing a correct card from the hand can be done in constant time. The class should support the following methods:
# - add_card(r, s): Add a new card with rank r and suit s to the hand.
# - play(s): Remove and return a card of suit s from the player's hand; if there is no card of suit s, then remove and return an arbitrary card from the hand.
# __iter__(): iterate through all cards currently in the hand.
# - all_of_suit(s): Iterate through all cards of suit s that are currently in the hand.

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

class CardHand:

    # ---------------------- nested _Card class ------------------------------ #
    class _Card:
        def __init__(self, rank, suit):
            self._rank = rank
            self._suit = suit

    # ---------------------- nonpublic utilities ------------------------------ #
    def _find_position(self, suit):
        walk = self._data.first()
        while walk is not None and walk.element()._suit != suit:
            walk = self._data.after(walk)
        return walk


    # ---------------------- public functions ------------------------------ #
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add_card(self, r, s):
        self._data.add_last(self._Card(r, s))

    def play(self, s):
        p = self._find_position(s)
        if p is not None:
            self._data.delete(p)
        else:
            if self.is_empty() == False:
                f = self._data.first()
                self._data.delete(f)

    def __iter__(self):
        cursor = self._data.first()
        while cursor is not None:
            print([cursor.element()._suit, cursor.element()._rank])
            cursor = self._data.after(cursor)

    def all_of_suit(self, s):
        walk = self._data.first()
        while walk is not None:
            if walk.element()._suit == s:
                print([walk.element()._suit, walk.element()._rank])
            walk = self._data.after(walk)


if __name__ in "__main__":
    Baibey = CardHand()
    Baibey.add_card(1, "spade")
    Baibey.add_card(7, "spade")
    Baibey.add_card(4, "heart")
    Baibey.add_card(10, "diamond")
    Baibey.add_card(4, "diamond")
    Baibey.add_card(1, "heart")
    Baibey.play("diamond")
    Baibey.play("club")
    Baibey.all_of_suit("heart")
    Baibey.all_of_suit("spade")
    Baibey.__iter__()
