class LinkedQueue:
    class _Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise 'empty'
        else:
            return self._head.element

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail.nxt = new

        self._tail = new
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise 'empty'
        else:
            answer = self._head.element
            self._head = self._head.nxt
            self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def is_empty(self):
        return self._size == 0

    # def __repr__(self):
