"""LIFO stack backed by a doubly-linked list."""


from __future__ import annotations
from typing import Optional, TypeVar

from ..core.base_linear import LinearBase
from ..core.nodes import LinearNode as Node
from ..core.exceptions import EmptyStructureError

T=TypeVar("T")


class Stack(LinearBase[T]):
    """a last-in-first-out stack with O(1) push/pop/peek.
    note: this overrides pop() with a no-argument LIFO version, which
    shadows LinearBase's indexed pop(index=-1).
    """

    def push(self,data:T) -> None:
        """push data onto the top of the stack: O(1)."""
        self._append_node(Node(data))

    def pop(self) -> T:  # type: ignore[override]
        """remove and return the top element: O(1)."""
        if not self._tail:
            raise EmptyStructureError("pop from empty stack")
        return self._remove_node(self._tail)

    def peek(self) -> Optional[T]:
        """return the top element without removing it, or None if empty."""
        return None if not self._tail else self._tail.data