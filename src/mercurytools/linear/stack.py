"""LIFO stack backed by a doubly-linked list."""


from ..core.base_linear import LinearBase
from ..core.nodes import LinearNode as Node
from ..core.exceptions import EmptyStructureError


class Stack(LinearBase):
    """a last-in-first-out stack with O(1) push/pop/peek.
    note: this overrides pop() with a no-argument LIFO version, which
    shadows LinearBase's indexed pop(index=-1).
    """

    def push(self,data):
        """push data onto the top of the stack: O(1)."""
        self._append_node(Node(data))

    def pop(self):
        """remove and return the top element: O(1)."""
        if not self._tail:
            raise EmptyStructureError("pop from empty stack")
        return self._remove_node(self._tail)

    def peek(self):
        """return the top element without removing it, or None if empty."""
        return None if not self._tail else self._tail.data