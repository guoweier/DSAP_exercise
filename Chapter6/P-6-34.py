# Implement a program that can input an expression in postfix notation (see Exercise C-6-22) and output its value.

class PostfixNotation:

    def __init__(self, expression):
        self._exp = expression
        self._S = []

    def calculate(self):
        for i in self._exp:
            if i.isdigit():
                self._S.append(i)
            else:
                v1 = self._S.pop()
                v2 = self._S.pop()
                self._S.append(str(eval(v2 + i + v1)))
        return float(self._S.pop())

if __name__ in "__main__":
    Exp = PostfixNotation("51+83-*4/")
    print(Exp.calculate())
