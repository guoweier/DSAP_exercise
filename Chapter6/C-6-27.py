# Suppose you have a stack S containing n elements a queue Q that is initially empty. Describe how you can use Q to scan S to see if it contain a certain element x, with the additional constrait that your algorithm must return the elements back to S in their original order. You may only use S, Q, and a constant number of other variables.

class ScanStack:

    def __init__(self, S, x):
        self._S = S
        self._Q = []
        self._x = x

    def S_empty(self):
        return len(self._S)==0

    def Q_empty(self):
        return len(self._Q)==0

    def push(self, value):
        self._S.append(value)

    def pop(self):
        if self.S_empty():
            raise Empty("Stack is empty.")
        else:
            return self._S.pop()

    def enqueue(self, value):
        return self._Q.append(value)

    def dequeue(self):
        if self.Q_empty():
            raise Empty("Queue is empty.")
        else:
            return self._Q.pop(0)

    def scan(self):
        while len(self._S):
            v = self._S.pop()
            if v == self._x:
                self.push(v)
                while len(self._Q):
                    q = self.dequeue()
                    self.push(q)
                return print((" ").join(["Stack contains target value",str(self._x)]))
            else:
                self.enqueue(v)
                if len(self._Q) > 1:
                    for i in range(len(self._Q)-1):
                        q = self.dequeue()
                        self.enqueue(q)

        while len(self._Q):
            q = self.dequeue()
            self.push(q)
        return print((" ").join(["Stack does not contain target value", str(self._x)]))

if __name__ in "__main__":
    S = [1,2,3,4]
    x = 5
    Data = ScanStack(S,x)
    Data.scan()
