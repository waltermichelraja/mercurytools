from ..core.base import LinearBase
from ..core.node import Node
from ..core.exceptions import EmptyStructureError


class Stack(LinearBase):
    def push(self,data):
        self._append_node(Node(data))

    def pop(self):
        if not self._tail:
            raise EmptyStructureError("pop from empty stack")
        return self._remove_node(self._tail)

    def peek(self):
        return None if not self._tail else self._tail.data