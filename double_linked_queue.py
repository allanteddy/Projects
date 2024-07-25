class _DoublyLinkedBase:
    class _Node:
        __slots__ = 'element', 'prev', 'nxt'

        def __init__(self, element, prev, nxt):
            self.element = element
            self.prev = prev
            self.nxt = nxt

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._trailer.prev = self._header
        self._header.nxt = self._trailer
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor.nxt = newest
        predecessor.prev = newest
        return newest

    def _delete_node(self, node):
        predecessor = node.prev
        successor = node.nxt
        predecessor.nxt = successor
        successor.prev = predecessor
        self._size -= 1
        element = node.element
        node.element = node.prev = node.nxt = None
        return element
