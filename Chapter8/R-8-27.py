# Give the output of the function parenthesize(T, T.root()), as described in Code Fragment 8.25, when T is the tree of Figure 8.8.

def parenthesize(T, p):
    # Print parenthesized representation of subtree of T rooted at p.
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')

# - (/ (x (+ (3, 1), 3), + (- (9, 5), 2)), + (x (3, - (7, 4)), 6))
