class ArrayStack:
    def __init__(self):
        # create an empty stack
        self._data = []

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise 'stack is empty'
        else:
            return self._data.pop()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise 'stack is empty'
        else:
            return self._data[-1]
