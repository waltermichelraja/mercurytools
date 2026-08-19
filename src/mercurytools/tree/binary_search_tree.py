"""unbalanced binary search tree."""


from __future__ import annotations
from typing import Optional, Tuple, TypeVar

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


    def _remove(self,node:Optional[Node[T]],value:T) -> Tuple[Optional[Node[T]],bool]:
        """recursively remove value from the subtree rooted at node.
        returns [new_subtree_root, was_deleted].
        """
        if not node:
            return node,False
        if value<node.data:
            node.left,deleted=self._remove(node.left,value)
            return node,deleted
        if value>node.data:
            node.right,deleted=self._remove(node.right,value)
            return node,deleted
        if not node.left and not node.right:
            return None,True
        if not node.left:
            return node.right,True
        if not node.right:
            return node.left,True
        successor=self._min_node(node.right)
        node.data=successor.data
        node.right,deleted=self._remove(node.right,successor.data)
        return node,True

    def _min_node(self,node:Node[T]) -> Node[T]:
        """return the leftmost [smallest] node in the subtree rooted at node."""
        while node.left:
            node=node.left
        return node


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
        """remove and return value: O(h)."""
        new_root,deleted=self._remove(self._root,value)
        self._set_root(new_root)
        if deleted:
            self._set_size(self._size-1)
            return value
        raise ValueNotFoundError(f"{value} not found")

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