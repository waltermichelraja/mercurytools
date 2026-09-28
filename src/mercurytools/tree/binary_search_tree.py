"""unbalanced binary search tree."""


from __future__ import annotations
from typing import Optional, TypeVar

from ..core.base_tree import TreeBase
from ..core.nodes import BinaryTreeNode as Node
from ..core.exceptions import ValueNotFoundError
from ..core.comparable import Comparable

T=TypeVar("T",bound=Comparable)


class BinarySearchTree(TreeBase[T]):
    """a classic [unbalanced] binary search tree.
    insert/remove/__contains__ are O(h) where h is the tree's height --
    O(log n) on average, but O(n) in the worst case for adversarial or
    already-sorted insertion order.
    """

    def __contains__(self,value:T) -> bool:
        """return True if value is present: O(h)."""
        current=self._root
        while current:
            if value<current.data:
                current=current.left
            elif value>current.data:
                current=current.right
            else:
                return True
        return False


    def insert(self,data:T) -> None:
        """insert data, maintaining BST ordering. Duplicate values are ignored: O(h)."""
        if not self._root:
            self._set_root(Node(data))
            self._set_size(self._size+1)
            return
        current=self._root
        while True:
            if data<current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=Node(data)
                    self._set_size(self._size+1)
                    return
            elif data>current.data:
                if current.right:
                    current=current.right
                else:
                    current.right=Node(data)
                    self._set_size(self._size+1)
                    return
            else:
                return

    def remove(self,value:T) -> T:
        """remove and return value: O(h). iterative [no recursion depth limit].
        raises ValueNotFoundError if value is absent.
        """
        parent:Optional[Node[T]]=None
        node=self._root
        while node:
            if value<node.data:
                parent,node=node,node.left
            elif value>node.data:
                parent,node=node,node.right
            else:
                break
        if not node:
            raise ValueNotFoundError(f"{value} not found")
        if node.left and node.right:
            # two children: copy the in-order successor up, then splice the successor out
            parent,successor=node,node.right
            while successor.left:
                parent,successor=successor,successor.left
            node.data=successor.data
            node=successor
        child=node.left if node.left else node.right
        if not parent:
            self._set_root(child)
        elif parent.left is node:
            parent.left=child
        else:
            parent.right=child
        self._set_size(self._size-1)
        return value

    def min(self) -> Optional[T]:
        """return the smallest value, or None if empty: O(h)."""
        if not self._root:
            return None
        node=self._root
        while node.left:
            node=node.left
        return node.data

    def max(self) -> Optional[T]:
        """return the largest value, or None if empty: O(h)."""
        if not self._root:
            return None
        node=self._root
        while node.right:
            node=node.right
        return node.data