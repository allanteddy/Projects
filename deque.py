from double_linked_queue import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise 'empty'
        else:
            return self._header.nxt.element

    def last(self):
        if self.is_empty():
            raise 'empty'
        else:
            return self._trailer.prev.element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header.nxt)

    def insert_last(self, e):
        self._insert_between(e, self._trailer.prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise 'empty'
        else:
            self._delete_node(self._header.nxt)

    def delete_last(self):
        if self.is_empty():
            raise 'empty'
        else:
            self._delete_node(self._trailer.prev)
