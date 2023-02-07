# Design an ADT for a tow-color, double-stack ADT that consists of two stacks - one "red" and one "blue" - and has as its operations color-coded versions of the regular stack ADT operations. For example, this ADT should support both a red push operation and a blue push operation. Give an efficient implementation of this ADT using a single array where capacity is set at some value N that is assumed to always be larger than the sizes of the red and blue stacks combined.

class ColorStack:

    N = 100

    def __init__(self):
        self._data = [None]*ColorStack.N
        self._redfront = 0
        self._blueback = 0
        self._redsize = 0
        self._bluesize = 0

    def redis_empty(self):
        return self._redsize == 0

    def blueis_empty(self):
        return self._bluesize == 0

    def red_top(self):
        if self.redis_empty():
            raise ValueError("Red stack is empty.")
        return self._data[self._redfront]

    def blue_top(self):
        if self.blueis_empty():
            raise ValueError("Blue stack is empty.")
        return self._data[self._blueback]

    def red_push(self, e):
        self._redfront = (self._redfront - 1) % len(self._data)
        self._data[self._redfront] = e
        self._redsize += 1

    def blue_push(self, e):
        self._blueback = (self._blueback + 1) % len(self._data)
        self._data[self._blueback] = e
        self._bluesize += 1

    def red_pop(self):
        if self.redis_empty():
            raise ValueError("Red stack is empty.")
        answer = self._data[self._redfront]
        self._redfront = (self._redfront + 1) % len(self._data)
        self._redsize -= 1
        return answer

    def blue_pop(self):
        if self.blueis_empty():
            raise ValueError("Blue stack is empty.")
        answer = self._data[self._blueback]
        self._blueback = (self._blueback - 1) % len(self._data)
        self._bluesize -= 1
        return answer

if __name__ in "__main__":
    S = ColorStack()
    for i in range(10):
        S.red_push(i)
        S.blue_push(i)
    print(S.red_top())
    print(S.blue_top())
    for i in range(3):
        S.red_pop()
    for i in range(6):
        S.blue_pop()
    print(S.red_top())
    print(S.blue_top())
