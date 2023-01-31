# Modify the ArrayQueue implementation so that the queue's capacity is limited to maxlen elements, where maxlen is an optional parameter to the constructor (that defaults to None). If enqueue is called when the queue is at full capacity, throw a Full exception (defined similarly to Empty.)

class Full(Exception):
    def __init__(self, message):
        return print(message)

class ArrayQueue:

    def __init__(self,maxlen):
        self._maxlen = maxlen
        self._data = [None]*self._maxlen
        self._size = 0
        self._front = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._maxlen

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._maxlen
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self.is_full():
            raise Full("Queue is full.")
        avail = (self._front + self._size) % self._maxlen
        self._data[avail] = e
        self._size += 1

if __name__ in "__main__":
    Q = ArrayQueue(5)
    for i in range(1,5):
        Q.enqueue(i)
    print(Q.enqueue(6))
    print(Q.first())
