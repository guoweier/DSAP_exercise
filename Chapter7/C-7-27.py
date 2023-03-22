# Give a recursive implementation of a singly linked list class, such that an instance of a nonempty list stores its first element and a reference to a list of remaining elements.

class LinkedList:

    class _Node:
        def __init__(self, element, ref):
            self._element = element
            self._ref = ref

    def __init__(self, L, i = 0):
        if i == len(L)-1:
            self._Node(L[i], None)
            return None
        else:
            L.pop(0)
            return self.__init__(L,i+1)

if __name__ in "__main__":
    L = [1,2,3,4,5]
    a = LinkedList(L)
    
