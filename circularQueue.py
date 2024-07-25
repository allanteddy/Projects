class CircularQueue:
    class _Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            new.next = new
        else:
            new.next = self._tail.nxt

        self._tail.nxt = new
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise 'empty'

        oldhead = self._tail.nxt
        if self._size == 1:
            self._tail = None
        else:
            self._tail.nxt = oldhead.nxt
        self._size -= 1
        return oldhead.nxt.element

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def rotate(self):
        if self._size > 1:
            self._tail = self._tail.nxt

    def first(self):
        if self.is_empty():
            raise 'empty'
        else:
            head = self._tail.nxt
            return head.element
