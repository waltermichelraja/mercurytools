from ..core.base import LinearBase
from ..core.node import Node
from ..core.exceptions import EmptyStructureError


class Deque(LinearBase):
    def append(self,data):
        self._append_node(Node(data))

    def appendleft(self,data):
        self._prepend_node(Node(data))

    def pop(self):
        if not self._tail:
            raise EmptyStructureError("pop from empty deque")
        return self._remove_node(self._tail)

    def popleft(self):
        if not self._head:
            raise EmptyStructureError("pop from empty deque")
        return self._remove_node(self._head)