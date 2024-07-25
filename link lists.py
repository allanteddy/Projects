class LinkedStack:
    # ------nested node class---------
    class _Node:
        # none public member of the node class
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ----stack method-----

    def __init__(self):
        # create an empty stack
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise 'empty '
        else:
            return self._head.element

    def pop(self):
        if self.is_empty():
            raise 'is empty'
        else:
            answer = self._head.element
            self._head = self._head.nxt
            self._size -= 1
            return answer


    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
