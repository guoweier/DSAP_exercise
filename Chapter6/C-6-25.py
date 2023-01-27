# Describe how to implement the queue ADT using two stacks as instance variables, such that all queue operations execute in amortized O(1) time. Give a formal proof of the amortized bound.

class QueueTwostacks:

    def __init__(self, q=[]):
        self._S1 = q
        self._S2 = []
