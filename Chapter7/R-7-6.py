# Suppose that x and y are references to nodes of circularly linked lists, although not necessarily the same list. Describe a fast algorithm for telling if x and y belong to the same list.

class CircularQueue:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self,e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 1:
            self._tail = self._tail._next

    def identify_node(self,e):
        node = self._tail
        while node._element != e:
            node = node._next
        return node

    def examnode(self,x,y):
        node = x
        while node._next != y and node._next != x:
            node = node._next
        if node._next == y:
            result = "x and y are in the same linked list."
        else:
            result = "x and y belong to different linked lists."
        return result

if __name__ in "__main__":
    Q1 = CircularQueue()
    Q2 = CircularQueue()
    for i in range(10):
        Q1.enqueue(i)
        Q2.enqueue(i+10)
    x = Q1.identify_node(4)
    y = Q2.identify_node(12)
    print(Q1.examnode(x,y))
