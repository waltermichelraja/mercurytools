"""structural typing helper for TypeVar bounds that require ordering [<, >].
used by BinarySearchTree and AVLTree, whose stored values must support
comparison for the tree to remain ordered. BinaryTree does not use
this -- it has no ordering requirement.
"""


from __future__ import annotations
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class Comparable(Protocol):
    """structural type for anything supporting < and > comparisons."""

    def __lt__(self,other:Any) -> bool: ...
    def __gt__(self,other:Any) -> bool: ...