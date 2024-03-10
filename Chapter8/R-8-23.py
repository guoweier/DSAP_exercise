# Let T be an ordered tree with more than one node. Is it possible that the preorder traversal of T visits the nodes in the same order as the postorder traversal of T? If so, give an example; otherwise, explain why this cannot ocur. Likewise, is it possible that the preorder traversal of T visits the nodes in the reverse order of the postorder traversal of T? If so, give an example; otherwise, explain why this cannot occur.

# It is impossible to have preorder traversal of T visits the nodes in the same order as the postoder traversal of T.
# Since T has more than one node. In preorder traversal, it is always starting with the root, while for postorder, as long as root has children, the visit of the root would be later than its children. And since it is ordered, so no possibility there are same order.
# In alternative approach, let's assume the preorder and postorder traversal can have the same order through their visits of the ordered tree T. The first visit of preorder traversal is the root, while the first visit of postorder traversal is the left most children. So root = left most children. This is conflict with the ordered tree feature, since ordered tree has the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. So the assumption is wrong. So preorder and postorder cannot have the same order.

# It is possible.
# example:
#      4
#    3 
#  2
# 1
