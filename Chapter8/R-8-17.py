# Show how to use the Euler tour traversal to compute the level number f(p), as defined in Section 8.3.2, of each position in a binary tree T.

#### EulerTour ####
class EulerTour:

    def __init__(self, tree):
        # Prepare an Euler tour template for given tree.
        self._tree = tree

    def tree(self):
        # Return reference to the tree being traversed.
        return self._tree

    def execute(self):
        # Perform the tour and return any result from post visit of root.
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        # Perform tour of subtree rooted at Position p.
        # p: Position of current node being visited.
        # d: depth of p in the tree.
        # path: list of indices of children on path from root to p.
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass

#### BinaryEulerTour ####
class BinaryEulerTour(EulerTour):
    # Abstract base class for performing Euler tour of a binary tree.
    # This version includes an additional _hook_invisit that is called after the tour of the left subtree (if any), yet before the tour pf the right subtree (if any).
    # Note: Right child is always assigned index 1 in path, even if no left sibling.
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        pass


class LevelNumber(BinaryEulerTour):
    def _hook_postvisit(self, p, d, path, results):
        addon = 1
        for i in path:
            addon += i*(2**(d-1-i))
        answer = 2**d-2+addon
        return answer



# TEST
# _tour("-", 0, path=[])
# results = [None, None]
# previsit "-"
# if self._tree.left("-") is not None (TRUE)
# path = [0]
# results[0] = _tour("/", 1, [0])
# results = [None, None]
# previsit "/"
# if self._tree.left("/") is not None (TRUE)
# path = [0,0]
# results[0] = _tour("x", 2, [0,0])
# results = [None, None]
# previsit "x"
# if self._tree.left("x") is not None (TRUE)
# path = [0,0,0]
# results[0] = _tour("+", 3, [0,0,0])
# results = [None, None]
# previsit "+"
# if self._tree.left("+") is not None (TRUE)
# path = [0,0,0,0]
# results[0] = _tour("3", 4, [0,0,0,0])
# results = [None, None]
# previsit "3"
# if self._tree.left("3") is not None (FALSE)
# invisit("3", 4, [0,0,0,0])
# if self._tree.right("3") is not None (FALSE)
# answer = _hook_postvisit("3", 4, [0,0,0,0], [None, None])
# return answer (15) results = [15, None]
# path = [0,0,0]
# invisit("+", 3, [0,0,0])
# if self._tree.right("+") is not None (TRUE)
# path = [0,0,0,1]
# results[1] = _tour("1", 4, [0,0,0,1])
# results = [None, None]
# previsit "1"
# if self._tree.left("1") is not None (FALSE)
# invisit("1", 4, [0,0,0,1])
# if self._tree._right("1") is not None (FALSE)
# answer = _hook_postvisit("1", 4, [0,0,0,1], [None, None])
# return answer (16) results = [15, 16]
# path = [0,0,0]
# answer = _hook_postvisit("+", 3, [0,0,0], [15,16])
# return answer (7) results = [7, None]
# path = [0,0]
# invisit("x", 2, [0,0])
# if self._tree.right(x) is not None (TRUE)
# path = [0,0,1]
# results[1] = _tour("3", 3, [0,0,1])
# results = [None, None]
# previsit "3"
# if self._tree.left("3") is not None (FALSE)
# invisit("3", 3, [0,0,1])
# if self._tree.right("3") is not None (FALSE)
# answer = _hook_postvisit("3", 3, [0,0,1], [7, None])
# return answer (8) results = [7,8]
