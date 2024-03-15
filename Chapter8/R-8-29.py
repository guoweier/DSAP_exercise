# Descrbe, in pseudo-code, an algorithm for computing the number of descendants of each node of a binary tree. The algorithm should be based on the Euler tour traversal.

# ------------------------------ Euler Tour ----------------------------------- #
class EulerTour:
    """Abstract base class for performing Euler tour of a tree.
    _hook_previsit and _hook_postvisit may be overridden by subclasses.
    """

    def __init__(self, tree):
        """Prepare an Euler tour template for given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.
        p: Position of current node being visited.
        d: depth of p in the tree.
        path: list of indices of children on path from root to p.
        """
        self._hook_previsit(p, d, path) # pre visit p
        results = []
        path.append(0) # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path)) # recur on child's subtree
            path[-1] += 1 # increment index
        path.pop() # remove extraneous index from end of path
        answer = self._hook_postvisit(p, d, path, results) # post visit p
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass

# ------------------- binary tree ---------------------------- #
class BinaryEulerTree(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree.
    This version includes an additional _hook_invist that is called after the tour of the left subtree(if any), yet before the tour of the right subtree (if any).
    Note: Right child is always assigned index 1 in path, even if no left sibling."""
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invist(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invist(self, p, d, path):
        pass

    def count_descendants(self):
        
