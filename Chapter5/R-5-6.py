# Our implementation of insert for the DynamicArray class, as given in Code Fragment 5.5, has the following inefficiency. In the case when a resize occurs, the resize operation takes time to copy all the elements from an old array to a new array, and then the subsequent loop in the body of insert shifts many of those elements. Give an improved implementation of the insert method, so that, in the cae of a resize, the elements are shifted into their final position during that operation, thereby avoiding the subsequent shifting.

import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array

    def __len__(self):
        "Return number of elements stored in the array."
        return self._n

    def __getitem__(self, k):
        "Return element at index k."
        if k < 0:
            self._A[(self._n-1)]
        elif 0 <= k < self._n:
            self._A[k]
        else:
            raise IndexError('invalid index')

    def insert(self, k, value):
        "Insert value at index k, shifting subsequent values rightward."
        # for simplicity, we assume 0 <= k <= n in this version
        if self._n == self._capacity:
            self._A = self._make_array(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def append(self, obj):
        "Add object to end of the array."
        if self._n == self._capacity:           # not enough room
            self._resize(2 * self._capacity)    # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self,c):                        # nonpublic utility
        "Resize internal array to capacity c."
        B = self._make_array(c)                 # new (bigger) array
        for k in range(self._n):                # for each existing value
            B[k] = self._A[k]
        self._A = B                             # use the bigger array
        self._capacity = c

    def _make_array(self,c):                    # nonpublic utility
        "Return new array with capacity c."
        return (c * ctypes.py_object)()

if __name__ in '__main__':
    u = DynamicArray()
    for i in range(20):
        u.append(i)
    u.insert(k=4,value="a")
    for item in u:
        print(item)
