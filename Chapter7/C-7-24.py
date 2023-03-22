# Give a complete Implementation of the stack ADT using a singly linked list that inlcudes a header sentinel.

class LinkedStack:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None,None)
        self._head = self._header._next
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self,e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise ValueError("Stack is empty.")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

if __name__ in "__main__":
    S = LinkedStack()
    for i in range(10):
        S.push(i)
    for j in range(3):
        S.pop()
    print(S.top())
