# Answer the following questions so as to justify Proposition 8.8.
# a. What is the minimum number of external nodes for a proper binary tree with height h? Justify your answer.
# b. What is the maximum number of external nodes for a proper binary tree with height h? Justify your answer.
# c. Let T be a proper binary tree with height h and n nodes. Show that log(n+1)-1 <= h <= (n-1)/2
# d. For which values of n and h can the above lower and upper bounds on h be attained with equality?

# a. The minimum numbr of external nodes for a proper binary tree with height h: h+1
# To have the least number of external nodes, each level has one node with two children and the other node as external. When at the last level, two nodes are both external. So for each level there is one external node, with the last level has two external node. So the number of external node with height h = h+1

# b. The maximum number of external nodes for a proper binary tree with height h: 2^h
# To have the largest number of external nodes, each level has both nodes with two children. So all the external nodes are at the last level. For level increased by 1, the nodes number times 2. At the last level, the nodes number = external nodes number = 2^h.

# c. T is a proper binary tree. If every node has two children, then n = 2^0 + 2^1 + 2^2 + ... + 2^h. So n+1 = 2^1 + 2^1 + 2^2 + ... + 2^h = 2^2 + 2^2 + 2^3 + ... + 2^h = 2^3 + 2^3 + 2^4 + ... +2^h = 2^(h+1). So h = log(n+1)-1. This is the time when h is smallest, because every node has two children. On the other hand, the time when h is largest, n = 1 + 2 + 2 + ... + 2 (with h number of 2) = 1+2h. So h = (n-1)/2.

# d. For lower boundary: for example, h = 3 and n = 15, h = 2 and n = 7, h = 4 and n = 31. For higher boundary: for example, h = 3 and n = 7, h = 2 and n = 5, h = 4 and n = 9. 
