# Justify Table 8.2, sumarizing the running time of the methods of a tree represented with a linked structure, by providing, for each method, a description of its implementation, and an analysis of its running time.

# len
# Running time: O(1)
def __len__(self):
    return self._size
# not size related. Directly output self._size variable.

# is_empty
# Running time: O(1)
def is_empty(self):
    return len(self) == 0
# not size related. The running time of len() is O(1), so by using len(self) following with the comparison with 0, the running time is still a constant.

# root
# Running time: O(1)
class _Node:
    __slots__ = '_element', '_parent'
    def __init__(self, element, parent=None, children_list=list()):
        self._element = element
        self._parent = parent

class Position(Tree.Position):
    def __init__(self, container, node):
        self._container = container
        self._node = node

    def element(self):
        return self._node._element

    def __eq__(self, other):
        return type(other) is type(self) and other._node is self._node

def _make_position(self, node):
    return self.Position(self, node) if node is not None else None

def root(self):
    return self._make_position(self._root)
# root() function is using a nonpublic function _make_position(), while _make_position() function uses nested class Position(). Both of these two steps are not size related. So the running time is a constant, which is O(1). self._root is defined in the __init__ for LinkedTree class, which is also O(1). So the running time for root() is O(1).

# is_root
# Running time: O(1)
def is_root(self, p):
    return self.root() == p
# not size related. Since root() function is O(1), then using this function to decide its equivalence to p is also O(1).

# is_leaf
# Running time: O(1)
def num_children(self, p):
    node = self._validate(p)
    num = len(self._node._container)
    return num

def is_leaf(self, p):
    return self.num_children(p) == 0
# is_leaf based on function num_children(). num_children() based on the parameter self._children_list, which has been defined in __init__().

# children(p)
# Running time: O(cp+1) cp denote the number of children of a position p.
def children(self,p):
    children = self._make_position(p)._container
    for c in children:
        yield self._make_position(c)
# This function includes a loop, while each step running time is a constant, but the number of looping is defined by the number of children in position p. So running time is O(cp+1).

# depth(p)
# Running time: O(dp+1) dp denotes the depth of p in the tree T.
def depth(self, p):
    if self.is_root(p):
        return 0
    else:
        return 1+self.depth(self.parent(p))
# This is a recursive function, which the running time depends on the recursion of position p's depth. So the running time is O(dp+1).

# height
# Running time: O(n)
def _height2(self, p):
    if self.is_leaf(p):
        return 0
    else:
        return 1+max(self._height2(c) for c in self.children(p))

def height(self, p=None):
    if p is None:
        p = self.root()
    return self._height2(p)
# The height() function depends on the nonpublic _height2() function. _height2() function is a recursive one, which depends on the number of children for each position. In the worst case, position p is the root. So it needs to go through all the nodes to count the height of the tree. So the running time is O(n). 
