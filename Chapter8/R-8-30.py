# The build_expression_tree method of the ExpressionTree class requires input that is an iterable of string tokens. We used a convenient example, '(((3+1)x4)/((9-5)+2))', in which each character is its own token, so that the string itself sufficed as input to build_expression_tree. In general, a string, such as '(35 + 14)', must be explicitly tokenized into list ['(', '35', '+', '14', ')'] so as to ignore whitespace and to recognize multidigit numbers as a single token. Write a utility method, tokenize(raw), that returns such a list of tokens for a raw string.


# ----------------------------------- Expression Tree --------------------------------------- #
class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree.
        In a single parameter form, token should be a leaf value (e.g. '42'), and the expression tree will have that value at an isolated node.
        In a three-parameter version, token should be an operator, and left and right should be existing ExpressionTree instances that become the operands for the binary operator.
        """
        super().__init__() # LinkedBinaryTree initialization
        if not isintance(token, str):
            raise TypeError('Token must be a string')
            self._add_root(token) # use inherited, nonpublic method
            if left is not None: # presumably three-parameter form
                if token not in '+-*x/':
                    raise ValueError('Token must be valid operator')
                self._attach(self.root(), left, right) # use inherited, nonpublic method

        def __str__(self):
            """Return string representation of the expression."""
            pieces = [] # sequence of piecewise strings to compose
            self._parenthesize_recur(self.root(), pieces)
            return ''.join(pieces)

        def _parenthesize_recur(self, p, result):
            """Append piecewise representation of p's subtree to resulting list."""
            if self.is_leaf(p):
                result.append(str(p.element())) # leaf value as a string
            else:
                result.append('(') # opening parenthesis
                self._parenthesize_recur(self.left(p), result) # left subtree
                result.append(p.element()) # operator
                self._parenthesize_recur(self.right(p), result) # right subtree
                result.append(')') # closing parenthesis


def build_expression_tree(tokens):
    """Return an ExpressionTree based upon by a tokenized expression."""
    S = [] # we use Python list as stack
    for t in tokens:
        if t in '+-x*/': # t is an operator symbol
            S.append(t) # push the operator symbol
        elif t not in '()': # consider t to be a literal
            S.append(ExpressionTree(t)) # push trivial tree storing value
        elif t == ')': # compose a new tree from three constituent parts
            right = S.pop() # right subtree as per LIFO
            op = S.pop() # operator symbol
            left = S.pop() # left subtree
            S.append(ExpressionTree(op, left, right)) # repush tree
        # we ignore a left parenthesis
    return S.pop()

def tokenize(raw):
    """Return a tokenized expression from a raw string."""
    
