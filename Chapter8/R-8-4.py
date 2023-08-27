# What is the running time of a call to T._height2(p) when called on a position p distinct from the root T? (See Code Fragment 8.5)

def _height2(self, p):
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height2(c) for c in self.childre(p))

# We assume such an algorithm is generated as O(cp+1) time, where p denotes the number of children of p. Algorithm _height2 spends O(cp+1) time at each position p to compute the maximum, and its overall running time is O(SUM(cp+1)) = O(n+SUM(cp)). Particularlly, SUM(cp) = n-1. So the running time on a position p distinct from the toot T is O(n+SUM(cp)) = O(n+n-1-croot) = O(2n-1-croot), where croot denotes to the children number of root. 
