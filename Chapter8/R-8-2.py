# Show a tree achieving the worst-case running time for algorithm depth.

# A tree with all the nodes form a single branch.

def depth(self, p):
    if self.is_root(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))

# the running time of T.depth(p) for position p is O(dp+1), with dp represents the depth of p in the tree T. The algorithm T.depth(p) runs in O(n) worst-case time, where n is the total number of positions of T. When dp = n, all the nodes form a single linear branch. 
