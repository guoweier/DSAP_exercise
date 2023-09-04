# Give a proof by induction of Proposition 8.9.
# In a nonempty proper binary tree T, with nE external nodes and nI internal nodes, we have nE = nI + 1.

# We separate nodes into two piles: internal nodes pile and external nodes pile.
# If there is only one node in tree T, it is the root and it is external. So tree T has 1 external node and 0 internal node. So nE = nI + 1.
# If tree T has more than one node, we remove from T an arbitrary external node w and its parent v, which is an internal node. We place w on the external node pile and v on the internal node pile. If v has a parent u, we reconnect u with the fomrer sibling z of w. This operation, removes one internal node and one external node. Repeating this operation, we eventually are left with a final tree consisting of a single node. Note that the same number of external and internal nodes, have been removed and placed on their respective piles by the response of operations leading to this final tree. Now, we remove the node of the final tree and we place it on the external node pile. Thus the external node pile has one more node than the internal node pile. 
