"""doubly-linked list."""


from __future__ import annotations
from typing import TypeVar

from ..core.base_linear import LinearBase
from ..core.nodes import LinearNode as Node
from ..core.exceptions import IndexOutOfBoundsError,ValueNotFoundError

T=TypeVar("T")


class LinkedList(LinearBase[T]):
    """a doubly-linked list supporting O(1) append/prepend and indexed insert/remove."""

    def append(self,data:T) -> None:
        """add data to the end: O(1)."""
        self._append_node(Node(data))

    def prepend(self,data:T) -> None:
        """add data to the start: O(1)."""
        self._prepend_node(Node(data))

    def insert(self,index:int,data:T) -> None:
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
            assert current is not None
            current=current.next
        assert current is not None and current.prev is not None
        node=Node(data)
        node.prev=current.prev
        node.next=current
        current.prev.next=node
        current.prev=node
        self._set_size(self._size+1)

    def remove(self,value:T) -> T:
        """remove and return the first element equal to value."""
        current=self._head
        while current:
            if current.data==value:
                return self._remove_node(current)
            current=current.next
        raise ValueNotFoundError(f"{value} not found")