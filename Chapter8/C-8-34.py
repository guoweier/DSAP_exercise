# For a tree T, let nI denote the number of its internal nodes, and let nE denote the number of its external nodes. Show that if every internal node in T has exactly 3 children, then nE=2nI+1.

# for each internal node, it has 3 children.
# Case1: If T has only one node, then it is the root. So nI=0, nE=1. nE=nI*2+1
# Case2: If T has more than one node. 
# If one child is external, that internal node can be substitude by one external. We can actually remove that internal node together with that external node.
# In this operation, we finally can left with a tree T only has one internal node (root), and has 3 children.
# So nE=3, nI=1. So nE=2*nI+1
