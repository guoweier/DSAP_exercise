# Our definition of the level numbering function f(p), as given in Section 8.3.2, began with the root having number 0. Some authors prefer to use a level numbering g(p) in which the root is assigned number 1, because it simplifies the arithmetic for finding neighboring positions. Redo Exercise R-8-18, but assuming that we use a level numbering g(p) in which the root is assigned number 1.

def g(p):
    return f(p)+1

def root():
    return A[1]

def parent(p):
    return A[(g(p)-1)//2]

def left(p):
    return A[2g(p)+1]

def right(p):
    return A[2g(p)+2]

def is_leaf(p):
    return (A[2g(p)+1]==None and A[2g(p)+2]==None)

def is_root(p):
    return g(p) == 1
