"""internal node types backing the linear and tree structures."""


from __future__ import annotations
from typing import Generic, Optional, TypeVar

T=TypeVar("T")
K=TypeVar("K")
V=TypeVar("V")


class LinearNode(Generic[T]):
    """a doubly-linked node used by LinearBase-derived structures [LinkedList, Stack, Deque]."""
    __slots__=("data","next","prev")

    def __init__(self,data:T) -> None:
        self.data:T=data
        self.next:Optional[LinearNode[T]]=None
        self.prev:Optional[LinearNode[T]]=None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.data})"


class LRUNode(Generic[K,V]):
    """a doubly-linked key/value node used internally by LRUCache."""
    __slots__=("key","value","prev","next")

    def __init__(self,key:K,value:V) -> None:
        self.key:K=key
        self.value:V=value
        self.prev:Optional[LRUNode[K,V]]=None
        self.next:Optional[LRUNode[K,V]]=None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.key}:{self.value})"


class BinaryTreeNode(Generic[T]):
    """a binary tree node used by BinaryTree, BinarySearchTree, and AVLTree."""
    __slots__=("data","left","right","height")

    def __init__(self,data:T) -> None:
        self.data:T=data
        self.left:Optional[BinaryTreeNode[T]]=None
        self.right:Optional[BinaryTreeNode[T]]=None
        self.height:int=1

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.data})"