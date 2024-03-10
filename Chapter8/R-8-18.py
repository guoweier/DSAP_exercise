# Let T be a binary tree with n positions that is realized with an array representation A, and let f() be the level numbering function of the positions of T, as given in Section 8.3.2. Give pseudo-code descriptions of each of the methods root, parent, left, right, is_leaf, and is_root.

def root():
    return A[0]

def parent(p):
    return A[(f(p)-1)//2]

def left(p):
    return A[2f(p)+1]

def right(p):
    return A[2f(p)+2]

def is_leaf(p):
    return (A[2f(p)+1]==None and A[2f(p)+2]==None)

def is_root(p):
    return f(p) == 0
