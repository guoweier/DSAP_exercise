# Add support in LinkedBinary Tree for a method, _delete_subtree(p), that removes the entire subtree rooted at position p, making sure to maintain the count on the size of the tree. What is the running time of your implementation?

# -------------------------------- class LinkedBinary Tree -------------------------------------- #
class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node: # Lightweight, nonpulic class for storing a node.
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return assocated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node: # convention for deprecated nodes
            vaise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)"""
        return self.Position(self, node) if node is not None else None

    # ---------------------- binary tree constructor -------------------------- #
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0
