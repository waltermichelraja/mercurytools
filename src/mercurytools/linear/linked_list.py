"""doubly-linked list."""


from ..core.base_linear import LinearBase
from ..core.nodes import LinearNode as Node
from ..core.exceptions import IndexOutOfBoundsError,ValueNotFoundError


class LinkedList(LinearBase):
    """a doubly-linked list supporting O(1) append/prepend and indexed insert/remove."""

    def append(self,data):
        """add data to the end: O(1)."""
        self._append_node(Node(data))

    def prepend(self,data):
        """add data to the start: O(1)."""
        self._prepend_node(Node(data))

    def insert(self,index,data):
        """insert data before the element currently at index."""
        if index<0 or index>self._size:
            raise IndexOutOfBoundsError()
        if index==0:
            self.prepend(data)
            return
        if index==self._size:
            self.append(data)
            return
        current=self._head
        for _ in range(index):
            current=current.next
        node=Node(data)
        node.prev=current.prev
        node.next=current
        current.prev.next=node
        current.prev=node
        self._set_size(self._size+1)

    def remove(self,value):
        """remove and return the first element equal to value."""
        current=self._head
        while current:
            if current.data==value:
                return self._remove_node(current)
            current=current.next
        raise ValueNotFoundError(f"{value} not found")