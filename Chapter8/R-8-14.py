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
class Position(Tree.Position):
    def __init__(self, container, node):
        self._container = container
        self._node = node

    def element(self):
        return self._node._element

    def __eq__(self, other):
        return type(other) is type(self) and other._node is self._node

def _make_position(self, node):
    return self.Position(self, node) is node is not None else None

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
def __init__(self):
    self._root = None
    self._size = 0
    self._children_list = []

def num_children(self, p):
    node = self._validate(p)
    num = len(self._children_list)
    return num

def is_leaf(self, p):
    return self.num_children(p) == 0
# is_leaf based on function num_children(). num_children() based on the parameter self._children_list, which has been defined in __init__().

# children(p)
# Running time: O(cp+1) cp denote the number of children of a position p.
