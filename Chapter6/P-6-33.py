# Give an array-based implementation of a double-ended queue supporting all of the public behaviors shown in Table 6.4 for the collection.deque class, including use of the maxlen optional parameter. When a length-limited deque is full, provide semantics similar to the collections.deque class, whereby a call to insert an element on one end of a deque causes an element to be lost from the opposite side.

class CollectionDeque:

    def __init__(self, maxlen):
        self._maxlen = maxlen
        self._data = [None]*self._maxlen
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def add_first(self, e):
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        if self._size < len(self._data):
            self._size += 1

    def add_last(self, e):
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        if self._size == len(self._data):
            self._front = (self._front + 1) % len(self._data)
        else:
            self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer

    def clear(self):
        self._data = [None]*self._maxlen

    def rotate(self, k):
        step1 = k % self._size
        step2 = self._size - step1
        if step1 <= step2:
            for i in range(step1):
                x = self.delete_last()
                self.add_first(x)
        else:
            for i in range(step2):
                x = self.delete_first()
                self.add_last(x)

    def remove(self, e):
        if self.is_empty():
            raise Empty("Deque is empty.")
        i = 0
        while i < self._size:
            locate = (self._front+i) % len(self._data)
            if self._data[locate] == e:
                for j in range(i, self._size):
                    p = (self._front+j) % len(self._data)
                    pn = (p+1) % len(self._data)
                    self._data[p] = self._data[pn]
                return
            i += 1

    def count(self, e):
        if self.is_empty():
            raise Empty("Deque is empty.")
        c = 0
        for i in range(self._size):
            locate = (self._front+i) % len(self._data)
            if self._data[locate] == e:
                c += 1
        return c


if __name__ in "__main__":
    dq = CollectionDeque(10)
    for i in range(9):
        dq.add_last(i)
    dq.rotate(1)
    print(dq.first())
    dq.add_last(5)
    print(dq.count(5))
    dq.remove(0)
    print(dq.first())
