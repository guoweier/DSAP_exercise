# What is the running time of parenthesize(T, T.root()), as given in Code Fragment 8.25, for a tree T with n nodes?

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

# if n = 1, O(n) = 1
# if n = 3, O(n) = 11
# if n = 5, O(n) = 21
# if n = 7, O(n) = 31
# if n = 9, O(n) = 41
# if n = 11, O(n) = 51
# ......
# Every time with 2 more chindren, where one leaf node has two children, O(n) + 10. In other orders, O((n-1)/2*10+1) = O(5n-4) = O(n).
# So the running time for parenthesize(T, T.root()) is O(n.)
