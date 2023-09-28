# Let T b a binary tree with n nodes, and let f() be the level numbering function of the positions of T, as given in Section 8.3.2.
# a. Show that, for every position p of T, f(p) <= 2^n-2
# b. Show an example of a binary tree with seven nodes that attains the above upper bound on f(p) for some position p.

# a. If p is the root of T, then f(p) = 0
# If p is the left child of position q, then f(p) = 2f(q)+1
# If p is the right child of position q, then f(p) = 2f(q)+2
# The worst case is that n nodes form into a linear tree, with each node be the right child. Left child are all missing. In thise case, nodes number represent the Tree depth. Since it is a binary tree, so the f(last child) = 2^0+2^1+2^2+2^3+...+2^(n-1)-1 = 1+2^0+2^1+2^2+...+2^(n-1)-1-1 = 2^1+2^1+2^2+...+2^(n-1)-2 = 2^2+2^3+2^4+...+2^(n-1)-2 = 2^n-2
# This is the worst case. So all the other case should be better than this.
# In general, f(p) <= 2^n-2.

# b. example
#               0
#                   2
#                       6
#                           14
#                               30
#                                   62
#                                       126
