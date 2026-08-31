"""disjoint-set [union-find] with path compression and union by size."""


from __future__ import annotations
from collections.abc import Hashable
from typing import Dict, Generic, Iterator, List, TypeVar

from ..core.exceptions import ValueNotFoundError

T=TypeVar("T",bound=Hashable)


class DisjointSet(Generic[T]):
    """tracks a partition of elements into disjoint sets, supporting near
    O(1) [amortized O(inverse-Ackermann(n))] find/union via path
    compression and union by size.
    """

    def __init__(self) -> None:
        self._parent:Dict[T,T]={}
        self._size:Dict[T,int]={}
        self._num_sets:int=0

    @property
    def num_sets(self) -> int:
        """number of disjoint sets currently tracked."""
        return self._num_sets

    def __len__(self) -> int:
        return len(self._parent)

    def __iter__(self) -> Iterator[T]:
        """iterate over every tracked element, in insertion order."""
        return iter(self._parent)

    def __contains__(self,x:T) -> bool:
        """return True if x is tracked: O(1)."""
        return x in self._parent

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self.groups())})"


    def make_set(self,x:T) -> None:
        """start tracking x as its own singleton set. a no-op if x is
        already tracked: O(1).
        """
        if x not in self._parent:
            self._parent[x]=x
            self._size[x]=1
            self._num_sets+=1

    def find(self,x:T) -> T:
        """return the representative element of x's set, compressing the
        path to it along the way: O(inverse-Ackermann(n)) amortized.
        """
        if x not in self._parent:
            raise ValueNotFoundError(f"{x!r} not found")
        root=x
        while self._parent[root]!=root:
            root=self._parent[root]
        while self._parent[x]!=root:
            next_x=self._parent[x]
            self._parent[x]=root
            x=next_x
        return root

    def union(self,x:T,y:T) -> None:
        """merge the sets containing x and y, adding either as a new
        singleton set first if not already tracked. a no-op if x and y
        are already in the same set: O(inverse-Ackermann(n)) amortized.
        """
        self.make_set(x)
        self.make_set(y)
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x==root_y:
            return
        if self._size[root_x]<self._size[root_y]:
            root_x,root_y=root_y,root_x
        self._parent[root_y]=root_x
        self._size[root_x]+=self._size[root_y]
        self._num_sets-=1

    def connected(self,x:T,y:T) -> bool:
        """return True if x and y are tracked and in the same set.
        returns False [rather than raising] if either isn't tracked,
        matching __contains__/has_* style checks elsewhere in this
        library: O(inverse-Ackermann(n)) amortized.
        """
        if x not in self._parent or y not in self._parent:
            return False
        return self.find(x)==self.find(y)

    def size_of(self,x:T) -> int:
        """return the number of elements in x's set: O(inverse-Ackermann(n)) amortized."""
        root=self.find(x)
        return self._size[root]

    def groups(self) -> Iterator[List[T]]:
        """yield each disjoint set's members as a list, one group per set."""
        buckets:Dict[T,List[T]]={}
        for x in self._parent:
            buckets.setdefault(self.find(x),[]).append(x)
        yield from buckets.values()

    def clear(self) -> None:
        """stop tracking all elements."""
        self._parent={}
        self._size={}
        self._num_sets=0