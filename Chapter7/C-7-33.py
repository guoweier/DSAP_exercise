# Modify the _DoublyLinkedBase class to include a reverse method that reverses the order of the list, yet without creating or destroying any nodes.

class _DoublyLinkedBase:

    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def reverse(self, node1="header", node2="trailer"):
        if node1 == "header":
            node1 = self._header
            node2 = self._trailer
        if node1 == node2:
            return self
        elif node1._next == node2 and node2._prev == node1:
            predecessor = node1._prev
            successor = node2._next
            predecessor._next = node2
            node2._prev = predecessor
            node2._next = node1
            node1._prev = node2
            node1._next = successor
            successor._prev = node1
            return self
        else:
            predecessor = node1._prev
            successor = node2._next
            node1_new = node1._next
            node2_new = node2._prev

            predecessor._next = node2
            node2._prev = predecessor
            node1._next = successor
            successor._prev = node1
            return self.reverse(node1_new, node2_new)
