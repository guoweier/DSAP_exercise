# Describe how to implement double ended queue ADT using two stacks as instance variables. What are the running times of the methods?

class DoubleEndQueue():

    def __init__(self,dq = []):
        self._S1 = dq
        self._S2 = []

    def is_empty(self):
        return len(self._S1)==0 and len(self._S2)==0

    def add_last(self, value):
        return self._S1.append(value)

    def add_first(self, value):
        if len(self._S2)==0 and len(self._S1) > 0:
            while len(self._S1):
                x = self._S1.pop()
                self._S2.append(x)
            return self._S2.append(value)
        else:
            return self._S2.append(value)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        elif len(self._S1)==0 and len(self._S2) > 0:
            while len(self._S2):
                x = self._S2.pop()
                self._S1.append(x)
            return self._S1.pop()
        else:
            return self._S1.pop()

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        elif len(self._S2)==0 and len(self._S1) > 0:
            while len(self._S1):
                x = self._S1.pop()
                self._S2.append(x)
            return self._S2.pop()
        else:
            return self._S2.pop()

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        elif len(self._S2)==0 and len(self._S1) > 0:
            while len(self._S1):
                x = self._S1.pop()
                self._S2.append(x)
            return self._S2[-1]
        else:
            return self._S2[-1]

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        elif len(self._S1)==0 and len(self._S2) > 0:
            while len(self._S2):
                x = self._S2.pop()
                self._S1.append(x)
            return self._S1[-1]
        else:
            return self._S1[-1]

if __name__ in "__main__":
    deque = DoubleEndQueue()
    deque.add_last(1)
    deque.add_first(2)
    deque.add_first(3)
    print(deque.delete_last())
    print(deque.delete_first())
    deque.add_first(4)
    print(deque.last())
