# Describe how to implement the queue ADT using two stacks as instance variables, such that all queue operations execute in amortized O(1) time. Give a formal proof of the amortized bound.

class QueueTwostacks:

    def __init__(self, q=[]):
        self._S1 = q
        self._S2 = []

    def is_empty(self):
        return len(self._S1)==0 and len(self._S2)==0

    def enqueue(self, value):
        return self._S1.append(value)

    def dequeue(self):
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

if __name__ in "__main__":
    q = QueueTwostacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.first())
    print(q.dequeue())
    print(q.first())
