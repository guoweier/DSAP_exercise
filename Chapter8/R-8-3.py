# Give a justification of Proposition 8.4.

# Proposition 8.4: The height of a nonempty tree T is equal to the maximum of the depths of its leaf positions.
# Let's assume the height of a nonempty tree T is not equal to the maximum of the depths of its leaf positions.
# The height of a nonempty tree T = the height of the root of T. With the definition of height, if p is a leaf, then the height of p is 0. Otherwise, the height of p is one more than the maximum of the heights of p's children. Since T is nonempty, so the height of p is one more than the heights of root's children. Following this definition, when all the children are leaves, then the height = 0. Then adding the 1s collected togehter from the previous layers, we get the height of tree T = the layer number - 1.
# From the definition of depth, the depth of p is the number of ancestors of p, excluding p itself. Leaves equal to the nodes without childre. Taking all the leaves within the tree T and count their ancestor numbers. Every time we go up one layer, that is counted as one ancestor. The maximum depths = the depth of nodes at the bottom layer = layer number - 1
# So the height of tree T = maximum depth of leaf positions.
# So we reject the initial hypothesis. The proposition 8.4 is correct.
