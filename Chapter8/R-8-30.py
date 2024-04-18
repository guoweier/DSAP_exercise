# The build_expression_tree method of the ExpressionTree class requires input that is an iterable of string tokens. We used a convenient example, '(((3+1)x4)/((9-5)+2))', in which each character is its own token, so that the string itself sufficed as input to build_expression_tree. In general, a string, such as '(35 + 14)', must be explicitly tokenized into list ['(', '35', '+', '14', ')'] so as to ignore whitespace and to recognize multidigit numbers as a single token. Write a utility method, tokenize(raw), that returns such a list of tokens for a raw string.

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

    # -------------- oncrete methods implemented in this class -------------- #
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position  does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

# ----------------------------------- BinaryTree -------------------------------------------- #
class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # ------------------------- additional abstract methods -------------------------- #
    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    # -------- concrete methods implemented in this class ------------- #
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None: # p must be the root
            return None # root has no sibling
        else:
            if p == self.left(parent): # possibly None
                return self.right(parent)
            else:
                return self.left(parent) # possibly None

    def children(self, p):
        """Generate an iteration of Position representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

# ----------------------------------- LinkedBinaryTree -------------------------------------- #
class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure. """
     class _Node: # Lightweigth, nonpublic class for storing a node.
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element. """

        def __init__(self, container, node):
            """Constructor should not be invoked by user. """
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position. """
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location. """
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid. """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._parent is p._node: # convention for deprecated nodes
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_posiiton(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # ----------------- binary tree constructor ---------------------- #
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # ----------------- public accessors ----------------------- #
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_posiiton(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is a root)."""
        node = self._validate(p)
        return self._make_posiiton(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_posiiton(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_posiiton(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None: # left child exists
            count += 1
        if node._right is not None: # right child exists
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists.')
        self._size = 1
        self._root = self._Node(e)
        return self._make_posiiton(self._root)

    def _add_left(self, p, e):
        """
        Create a new left child for Posiiton p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists.')
        self._size += 1
        node._left = self._Node(e, node) # node is its parent
        return self._make_posiiton(node._left)

    def _add_right(self, p, e):
        """
        Create a new right child for Posiiton p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists.')
        self._size += 1
        node._right = self._Node(e, node) # node is its parent
        return self._make_posiiton(node._right)

    def _replace(self, p, e):
        """Replace the elemnt at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """
        Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children.')
        child = node._left if node._left else node._right # might be None
        if child is not None:
            child._parent = node._parent # child's grandparent becomes parent
        if node is self._root:
            self._root = child # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node # convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf.')
        if not type(self) is type(t1) is type(t2): # all 3 trees must be same type
            raise TypeError('Tree types must match.')
        self._size += len(t1)+len(t2)
        if not t1.is_empty(): # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty(): # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None # set t2 instance to empty
            t2._size = 0

# ----------------------------------- Expression Tree --------------------------------------- #
class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree.
        In a single parameter form, token should be a leaf value (e.g. '42'), and the expression tree will have that value at an isolated node.
        In a three-parameter version, token should be an operator, and left and right should be existing ExpressionTree instances that become the operands for the binary operator.
        """
        super().__init__() # LinkedBinaryTree initialization
        if not isintance(token, str):
            raise TypeError('Token must be a string')
            self._add_root(token) # use inherited, nonpublic method
            if left is not None: # presumably three-parameter form
                if token not in '+-*x/':
                    raise ValueError('Token must be valid operator')
                self._attach(self.root(), left, right) # use inherited, nonpublic method

        def __str__(self):
            """Return string representation of the expression."""
            pieces = [] # sequence of piecewise strings to compose
            self._parenthesize_recur(self.root(), pieces)
            return ''.join(pieces)

        def _parenthesize_recur(self, p, result):
            """Append piecewise representation of p's subtree to resulting list."""
            if self.is_leaf(p):
                result.append(str(p.element())) # leaf value as a string
            else:
                result.append('(') # opening parenthesis
                self._parenthesize_recur(self.left(p), result) # left subtree
                result.append(p.element()) # operator
                self._parenthesize_recur(self.right(p), result) # right subtree
                result.append(')') # closing parenthesis


def build_expression_tree(tokens):
    """Return an ExpressionTree based upon by a tokenized expression."""
    S = [] # we use Python list as stack
    for t in tokens:
        if t in '+-x*/': # t is an operator symbol
            S.append(t) # push the operator symbol
        elif t not in '()': # consider t to be a literal
            S.append(ExpressionTree(t)) # push trivial tree storing value
        elif t == ')': # compose a new tree from three constituent parts
            right = S.pop() # right subtree as per LIFO
            op = S.pop() # operator symbol
            left = S.pop() # left subtree
            S.append(ExpressionTree(op, left, right)) # repush tree
        # we ignore a left parenthesis
    return S.pop()

def tokenize(raw):
    """Return a tokenized expression from a raw string."""
    S = []
    for i in range(len(raw)):
        if raw[i] in "+-x*/":
            S.append(raw[i])
        elif raw[i] == " ":
            continue
        elif raw[i] not in '()':
            N = [raw[i]]
            while (raw[i+1] != " ") and (raw[i+1] not in "+-x*/") and (raw[i+1] not in "()"):
                N.append(raw[i+1])
                i += 1
            literal = ''.join(N)
            S.append(literal)
    tokens = ''.join(S)
    return build_expression_tree(tokens)
