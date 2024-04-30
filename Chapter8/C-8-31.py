# Define the internal path length, I(T), of a tree T to be the sum of the depths of all the internal position in T. Likewise, define the external path length, E(T), of a tree T to be the sum of the depths of all the external positions in T. Show that if T is a proper binary tree with n positions, then E(T) = I(T) + n - 1.

# ----------------------------------- Tree ----------------------------------- #
class Tree:
    """Abstract base class representing a tree structure."""

    # ------------------------ nested Position class -------------------------- #
    class Position:
        """An abstraction representing the location of a single element."""

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

    # -------------- methods for counting internal and external nodes depth ---------------- #
    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1+self.depth(self.parent(p))

    def internal(self):
        """Generate the depth sum of internal nodes in the tree."""
        SUM = 0
        if not self.is_empty():
            for p in self._subtree_internal(self.root(), SUM):
                if not self.is_leaf(p):
                    SUM += self.depth(p)
        return SUM

    def _subtree_internal(self, p, SUM):
        """Generate the depth sum of internal nodes in subtree rooted at p."""
        if not self.is_leaf(p):
            SUM += self.depth(p)
        for c in self.children(p):
            for other in self._subtree_internal(c, SUM):
                if not self.is_leaf(other):
                    SUM += self.depth(other)

    def external(self):
        """Generate the depth sum of external nodes in the tree."""
        SUM = 0
        if not self.is_empty():
            for p in self._subtree_internal(self.root(), SUM):
                if self.is_leaf(p):
                    SUM += self.depth(p)
        return SUM

    def _subtree_external(self, p, SUM):
        """Generate the depth sum of external nodes in subtree rooted at p."""
        if self.is_leaf(p):
            SUM += self.depth(p)
        for c in self.children(p):
            for other in self._subtree_external(c, SUM):
                if self.is_leaf(other):
                    SUM += self.depth(other)

# --------------------------- depth sum of internal nodes --------------------------- #
def I(T):
    return T.internal()

def E(T):
    return T.external()


# Proposition: if T is a proper binary tree with n positions, then E(T) = I(T) + n - 1.
# Justification:
# Because in a nonempty proper binary tree T, with nE external nodes and nI internal nodes, we have nE = nI + 1. Then if there are in total n positions, nE = (n+1)/2, nI = (n-1)/2.
