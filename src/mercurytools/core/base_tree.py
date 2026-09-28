"""shared base class for binary tree structures [BinaryTree, BinarySearchTree, AVLTree]."""


from __future__ import annotations
from collections import deque
from typing import Generic, Iterator, List, Optional, TypeVar

from .base import InternalStateGuard
from .nodes import BinaryTreeNode as Node

T=TypeVar("T")


class TreeBase(InternalStateGuard,Generic[T]):
    """common state and traversal methods shared by all binary tree types."""
    _protected_fields=frozenset({"_root","_size"})
    _root:Optional[Node[T]]
    _size:int

    def __init__(self) -> None:
        object.__setattr__(self,"_root",None)
        object.__setattr__(self,"_size",0)

    @property
    def size(self) -> int:
        """number of elements currently stored."""
        return self._size

    @property
    def root(self) -> Optional[Node[T]]:
        """the root node, or None if the tree is empty."""
        return self._root
    
    def __contains__(self,value:T) -> bool:
        """return True if value is present: O(n) here; 
        overridden with O(h) in ordered trees.
        """
        return any(item==value for item in self)

    def __iter__(self) -> Iterator[T]:
        """iterate over stored values in-order [left, node, right]: O(n) here; 
        overridden with O(h) in ordered trees.
        """
        return self.inorder()

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self.inorder())})"
    

    def inorder(self) -> Iterator[T]:
        """yield values in-order: left subtree, node, right subtree.
        iterative [no recursion depth limit]: O(n) time, O(h) extra space.
        """
        stack:List[Node[T]]=[]
        node=self._root
        while stack or node:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            yield node.data
            node=node.right

    def preorder(self) -> Iterator[T]:
        """yield values pre-order: node, left subtree, right subtree.
        iterative [no recursion depth limit]: O(n) time, O(h) extra space.
        """
        if not self._root:
            return
        stack:List[Node[T]]=[self._root]
        while stack:
            node=stack.pop()
            yield node.data
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def postorder(self) -> Iterator[T]:
        """yield values post-order: left subtree, right subtree, node.
        iterative [no recursion depth limit]: O(n) time, O(h) extra space.
        """
        stack:List[Node[T]]=[]
        node=self._root
        last:Optional[Node[T]]=None
        while stack or node:
            if node:
                stack.append(node)
                node=node.left
                continue
            top=stack[-1]
            if top.right and last is not top.right:
                node=top.right
            else:
                yield top.data
                last=stack.pop()

    def level_order(self) -> Iterator[T]:
        """yield values breadth-first, level by level, top to bottom."""
        if not self._root:
            return
        q=deque([self._root])
        while q:
            current=q.popleft()
            yield current.data
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    def min(self) -> Optional[T]:
        """return the smallest value in the tree, or None if empty: O(n) here."""
        if self._size==0:
            return None
        return min(self)  # type: ignore[type-var]

    def max(self) -> Optional[T]:
        """return the largest value in the tree, or None if empty: O(n) here."""
        if self._size==0:
            return None
        return max(self)  # type: ignore[type-var]

    def height(self) -> int:
        """return the tree's height
        -- an empty tree has height -1, a single node has height 0.
        iterative [no recursion depth limit]: O(n).
        """
        if not self._root:
            return -1
        level=[self._root]
        height=-1
        while level:
            height+=1
            level=[child for node in level for child in (node.left,node.right) if child]
        return height

    def clear(self) -> None:
        """remove all elements"""
        object.__setattr__(self,"_root",None)
        object.__setattr__(self,"_size",0)

    def _set_root(self,node:Optional[Node[T]]) -> None:
        """set _root, bypassing the InternalStateGuard write-protection."""
        object.__setattr__(self,"_root",node)

    def _set_size(self,value:int) -> None:
        """set _size, bypassing the InternalStateGuard write-protection."""
        object.__setattr__(self,"_size",value)