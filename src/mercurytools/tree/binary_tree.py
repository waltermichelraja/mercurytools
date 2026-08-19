"""unordered binary tree with level-order [complete-tree] insertion."""


from __future__ import annotations
from collections import deque
from typing import TypeVar

from ..core.nodes import BinaryTreeNode as Node
from ..core.base_tree import TreeBase

T=TypeVar("T")


class BinaryTree(TreeBase[T]):
    """a generic binary tree with no ordering guarantee between parent and children.
    insert() always fills the first available slot in level order 
    [i.e. keeps the tree "complete"].
    """

    def insert(self,data:T) -> None:
        """insert data into the first open slot found in level [breadth-first] order. O(n)."""
        new_node=Node(data)
        if not self._root:
            self._set_root(new_node)
            self._set_size(self._size+1)
            return
        q=deque([self._root])
        while q:
            current=q.popleft()
            if not current.left:
                current.left=new_node
                self._set_size(self._size+1)
                return
            else:
                q.append(current.left)
            if not current.right:
                current.right=new_node
                self._set_size(self._size+1)
                return
            else:
                q.append(current.right)