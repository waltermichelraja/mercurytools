"""standalone binary heap [min or max], operating directly on comparable elements."""


from __future__ import annotations
from typing import Generic, Iterable, Iterator, List, Optional, TypeVar

from ..core.exceptions import EmptyStructureError
from ..core.comparable import Comparable

T=TypeVar("T",bound=Comparable)


class Heap(Generic[T]):
    """a binary heap over directly-comparable elements, min-heap by default.
    unlike PriorityQueue, there is no separate priority key or FIFO
    tie-breaking here -- Heap compares elements with each other directly
    via < and >, and ties may surface in either order.
    """

    def __init__(self,min_heap:bool=True) -> None:
        self._data:List[T]=[]
        self._min_heap:bool=min_heap

    @classmethod
    def from_iterable(cls,iterable:Iterable[T],min_heap:bool=True) -> "Heap[T]":
        """build a heap from iterable's elements in O(n), rather than
        O(n log n) from repeated push() calls.
        """
        heap:Heap[T]=cls(min_heap)
        heap._data=list(iterable)
        for i in reversed(range(len(heap._data)//2)):
            heap._heapify_down(i)
        return heap

    @property
    def is_min_heap(self) -> bool:
        """True if this heap pops the smallest element first; False for largest first."""
        return self._min_heap

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        kind="min" if self._min_heap else "max"
        return f"{self.__class__.__name__}({kind}, {self._data})"

    def __iter__(self) -> Iterator[T]:
        """iterate over stored values in raw heap-array order [not sorted]."""
        return iter(self._data)

    def __contains__(self,value:T) -> bool:
        """return True if value is present, using == comparison: O(n)."""
        return value in self._data

    def __eq__(self,other:object) -> bool:
        """two heaps are equal if they're the same kind [min/max] and hold
        the same multiset of values, regardless of internal array order.
        """
        if not isinstance(other,Heap):
            return False
        if self._min_heap!=other._min_heap:
            return False
        return sorted(self._data)==sorted(other._data)


    def push(self,value:T) -> None:
        """push value onto the heap: O(log n)."""
        self._data.append(value)
        self._heapify_up(len(self._data)-1)

    def pop(self) -> T:
        """remove and return the smallest element [largest, for a max-heap]: O(log n)."""
        if not self._data:
            raise EmptyStructureError("pop from empty heap")
        self._swap(0,len(self._data)-1)
        value=self._data.pop()
        self._heapify_down(0)
        return value

    def peek(self) -> Optional[T]:
        """return the smallest [or largest] element without removing it, or None if empty: O(1)."""
        return self._data[0] if self._data else None

    def to_list(self) -> List[T]:
        """return stored values as a plain list, in raw heap-array order [not sorted]."""
        return list(self._data)

    def clear(self) -> None:
        """remove all elements."""
        self._data=[]

    def copy(self) -> "Heap[T]":
        """return a new, independent heap with the same contents and mode."""
        new:Heap[T]=Heap(self._min_heap)
        new._data=list(self._data)
        return new


    def _before(self,a:T,b:T) -> bool:
        """return True if a should sit above b in this heap's ordering
        [smaller for a min-heap, larger for a max-heap].
        """
        return a<b if self._min_heap else a>b

    def _parent(self,i:int) -> int:
        return (i-1)//2

    def _left(self,i:int) -> int:
        return 2*i+1

    def _right(self,i:int) -> int:
        return 2*i+2

    def _swap(self,i:int,j:int) -> None:
        self._data[i],self._data[j]=self._data[j],self._data[i]

    def _heapify_up(self,i:int) -> None:
        """restore the heap property by bubbling the item at index i upward."""
        while i>0:
            p=self._parent(i)
            if self._before(self._data[i],self._data[p]):
                self._swap(i,p)
                i=p
            else:
                break

    def _heapify_down(self,i:int) -> None:
        """restore the heap property by sinking the item at index i downward."""
        size=len(self._data)
        while True:
            left=self._left(i)
            right=self._right(i)
            best=i
            if left<size and self._before(self._data[left],self._data[best]):
                best=left
            if right<size and self._before(self._data[right],self._data[best]):
                best=right
            if best!=i:
                self._swap(i,best)
                i=best
            else:
                break