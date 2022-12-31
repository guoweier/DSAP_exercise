# Postfix notation is an unambiguous way of writing an arithmetic expression without parentheses. It is defined so that if "(exp1)op(exp2)" is a normal, fully parenthesized expression whose operation is op, the postfix version of this is "pexp1 pexp2 op", where pexp1 is the postfix version of exp1 and pexp2 is the postfix version of exp2. The post fix version of a single number or variable is just that number or variable. For example, the postfix version of "((5+2)*(8-3))/4" is "5 2 + 8 3 - * 4 /". Describe a nonrecursive way of evaluating an expression in postfix notation.

def is_postfix(expr):
    S = ArrayStack()
    for i in reversed(range(len(expr)))
