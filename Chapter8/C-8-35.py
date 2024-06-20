# Two ordered trees T' and T'' are said to be isomorphic if one of the following holds:
# - Both T' and T'' are empty.
# - The roots of T' and T'' have the same number k >= 0 of substrees, and the ith such subtree of T' is isomorphic to the ith such subtree of T'' for i=1,2,3...k
# Design an algorithm that test whether two given ordered trees are isomorphic. What is the running time of your algorithm?

# The subtree needs to have at least one child. So the number of subtrees are equivalent to the number of internal nodes.
# So the second condition can be substitue to:
# - The roots of T' and T'' have the same nI, and all their internal nodes have the same nI.

# ----------------------------------- Tree ----------------------------------- #
class Tree:
    """Abstract base class representing a tree structure."""

    # ------------------------ nested Position class -------------------------- #
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored in this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True of other does not represent the same location."""
            return not (self == other) # opposite of __eq__

    # -------- abstract methods that concrete subclass must support ----------- #
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing the tree's parent (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Position representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # -------------- concrete methods implemented in this class -------------- #
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position  does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    # -------------- methods for counting the number of internal nodes ---------------- #
    def count_internal(self, p, SUM=0):
        """Generate the sum of internal nodes in the tree."""
        if self.is_leaf(p):
            return SUM
        else:
            for c in self.children(p):
                return self.count_internal(c, SUM+1)


# ------------ Function for define two trees if they are isomorphic --------------- #
def _count_subtree_internal(T, p=T.root(), internal_dict={}):
    if p.is_leaf():
        internal_dict[p] = 0
        return internal_dict
    else:
        for c in T.chilren(p):
            SUM = T.count_internal(c)
            internal_dict[c] = SUM
            return T._count_subtree_internal(c, internal_dict)


def isomorphic(T1,T2):
    if T1.is_empty() and T2.is_empty():
        return True
    elif T1._count_subtree_internal()==T2._count_subtree_internal():
        return True
    else:
        return False
