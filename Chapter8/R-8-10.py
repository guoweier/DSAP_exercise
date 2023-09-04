# Give a direct implementation of the num_children method within the class BinaryTree.

class Tree:
    # ------------------------ nested Position class ---------------------------- #
    def element(self):
        # Return the element sotred at this Position.
        raise NotImplementedError('Must be implemented by subclass.')

    def __eq__(self, other):
        # Return True if other Position represent the same location.
        raise NotImplementedError('Must be implemented by subclass.')

    def __ne__(self, other):
        # Return True if other does not represent the same location.
        return not (self == other)

    # ---------------- abstract methods that concrete subclass must support ------------------ #
    def root(self):
        # Return Position representing the tree's root (or None if empty)
        raise NotImplementedError('Must be implemented by subclass.')

    def parent(self, p):
        # Return Position representing p's parent (or None if empty)
        raise NotImplementedError('Must be implemented by subclass.')

    def num_children(self, p):
        # Return the number of children that Position p has.
        raise NotImplementedError('Must be implemented by subclass.')

    def children(self, p):
        # Generate an iteration of Position representingp's children.
        raise NotImplementedError('Must be implemented by subclass.')

    def __len__(self):
        # Return the total number of elements in the tree.
        raise NotImplementedError('Must be implemented by subclass.')

    # ------------- concrete methods implemented in this class -------------------- #
    def is_root(self, p):
        # Return True if Position p represents the root of the tree.
        return self.root() == p

    def is_leaf(self, p):
        # Return True if Position p does not have any children.
        return self.num_children(p) == 0

    def is_empty(self):
        # Return True if the tree is empty.
        return len(self) == 0


class BinaryTree(Tree):
    # ------------------------------ additional abstract methods ---------------------------------------- #
    def left(self, p):
        raise NotImplementedError('Must be implemented by subclass.')

    def right(self, p):
        raise NotImplementedError('Must be implemented by subclass.')

    # ---------------- concrete methods implemented in this class ------------------- #
    def sibling(self, p):
        # Return a Position representing p's sibling (or None if no sibling)
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        # Generate an interation of Positions representing p's children.
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def num_children(self, p):
        # Return the number of children that Position P has.
        num = 0
        if self.left(p) is not None:
            num += 1
        if self.right(p) is not None:
            num += 1
        return num
