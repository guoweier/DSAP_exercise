# Postfix notation is an unambiguous way of writing an arithmetic expression without parentheses. It is defined so that if "(exp1)op(exp2)" is a normal, fully parenthesized expression whose operation is op, the postfix version of this is "pexp1 pexp2 op", where pexp1 is the postfix version of exp1 and pexp2 is the postfix version of exp2. The post fix version of a single number or variable is just that number or variable. For example, the postfix version of "((5+2)*(8-3))/4" is "5 2 + 8 3 - * 4 /". Describe a nonrecursive way of evaluating an expression in postfix notation.

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        "Creat an empty stack."
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0


    def push(self,e):
        """Add element e to the top of the stack.
        """
        return self._data.append(e)

    def top(self):
        """Return (but not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is full.')
        return self._data.pop()


def is_postfix(expr):
    # set stack
    Snum = ArrayStack()
    # scan elements in expression
    for i in expr:
        if i.isdigit():
            Snum.push(i)
        else:
            value1 = Snum.pop()
            value2 = Snum.pop()
            Snum.push(str(eval(value2 + i + value1)))
    return float(Snum.pop())


if __name__ in "__main__":
    result = is_postfix("52+83-*4/")
    print(result)
