# We can simplify parts of our LinkedBinaryTree implementation if we make use of a single sentinel node, referenced as the _sentinel member of the tree instance, such that the sentinel is the parent of the real root of the tree, and the root is referenced as the left child of the sentinel. Furthermore, the sentinel will take the place of None as the value of the _left or _right member for a node without such a child. Give a new implementation of the update methods _delete and _attach, assuming such a representation.

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
        self._sentinel = self._Node(None,None,None,None)
        self._size = 0

    # ---------------------- public accessors -------------------------- #
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)"""
        return self._make_position(self._sentinel._left)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._sentinel._left is not None: raise ValueError('Root exists')
        self._size = 1
        self._sentinel._left = self._Node(e)
        return self._make_position(self._sentinel._left)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p)==2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._sentinel._left:
            self._sentinel._left = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1)+len(t2)
        if not t1.is_empty():
            t1._sentinel = node
            node._left = t1._sentinel._left
            t1._sentinel._left = None
            t1._size = 0
        if not t2.is_empty():
            t2._sentinel = node
            node._right = t2._sentinel._left
            t2._sentinel._left = None
            t2._size = 0


# --------------------------------- class BinaryTree --------------------------------------- #
class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # ----------------------- additional abstract methods ------------------------ #
    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        raise NotImplementError('must be implemented by subclass')

    # ------------------------- concrete methods implemented in this class ------------------------ #
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def children(self, p):
        """Generate an iteration of Positions representingp's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yeild self.right(p)

# --------------------------------- class Tree -------------------------------------- #
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
