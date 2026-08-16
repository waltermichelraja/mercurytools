"""double-ended queue backed by a doubly-linked list."""


from ..core.base_linear import LinearBase
from ..core.nodes import LinearNode as Node
from ..core.exceptions import EmptyStructureError


class Deque(LinearBase):
    """a double-ended queue with O(1) push/pop from either end.
    note: this overrides pop() with a no-argument version, which
    shadows LinearBase's indexed pop(index=-1).
    """

    def append(self,data):
        """add data to the right end: O(1)."""
        self._append_node(Node(data))

    def appendleft(self,data):
        """add data to the left end: O(1)."""
        self._prepend_node(Node(data))

    def pop(self):
        """remove and return the rightmost element: O(1)."""
        if not self._tail:
            raise EmptyStructureError("pop from empty deque")
        return self._remove_node(self._tail)

    def popleft(self):
        """remove and return the leftmost element: O(1)."""
        if not self._head:
            raise EmptyStructureError("pop from empty deque")
        return self._remove_node(self._head)