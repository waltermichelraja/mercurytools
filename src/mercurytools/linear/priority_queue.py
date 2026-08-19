"""binary min-heap priority queue, with an optional FIFO fallback mode."""


from __future__ import annotations
from typing import Any, Generic, Iterator, List, Optional, Tuple, TypeVar

from ..core.exceptions import EmptyStructureError

T=TypeVar("T")


class PriorityQueue(Generic[T]):
    """a binary min-heap that pops the lowest-priority value first.
    a single instance cannot mix priority andnon-priority pushes 
    -- whichever style is used first locks in the mode 
    for that instance's lifetime [until clear()].
    ties [equal priority] are broken by insertion order [FIFO], so the
    queue is stable.
    """

    def __init__(self) -> None:
        self._data:List[Tuple[Any,int,T]]=[]
        self._uses_priority:Optional[bool]=None
        self._counter:int=0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({[item[2] for item in self._data]})"

    def __iter__(self) -> Iterator[T]:
        """iterate over stored values in raw heap-array order [not priority order]."""
        for item in self._data:
            yield item[2]

    def __contains__(self,value:T) -> bool:
        """return True if value is present, using == comparison: O(n)."""
        return any(item[2]==value for item in self._data)

    def __eq__(self,other:object) -> bool:
        """two queues are equal if they'd pop in the same value sequence.
        compares both queues sorted by [priority, insertion order], so
        equal contents pushed in a different order still compare equal.
        """
        if not isinstance(other,PriorityQueue):
            return False
        if len(self)!=len(other):
            return False
        self_sorted=sorted(self._data,key=lambda item:(item[0],item[1]))
        other_sorted=sorted(other._data,key=lambda item:(item[0],item[1]))
        return [item[2] for item in self_sorted]==[item[2] for item in other_sorted]

    def push(self,value:T,priority:Optional[Any]=None) -> None:
        """push value with an optional priority [lower pops first]: O(log n)."""
        if self._uses_priority is None:
            self._uses_priority=priority is not None
        elif (priority is not None)!=self._uses_priority:
            raise ValueError("cannot mix priority and non-priority values")
        if priority is None:
            entry=(value,self._counter,value)
        else:
            entry=(priority,self._counter,value)
        self._counter+=1
        self._data.append(entry)
        self._heapify_up(len(self._data)-1)

    def pop(self) -> T:
        """remove and return the lowest-priority value."""
        if not self._data:
            raise EmptyStructureError("pop from empty priority queue")
        self._swap(0,len(self._data)-1)
        _,_,value=self._data.pop()
        self._heapify_down(0)
        return value

    def peek(self) -> Optional[T]:
        """return the lowest-priority value without removing it, or None if empty: O(1)."""
        if not self._data:
            return None
        return self._data[0][2]

    def to_list(self) -> List[T]:
        """return stored values as a plain list, in raw heap-array order [not priority order]."""
        return [item[2] for item in self._data]

    def clear(self) -> None:
        """remove all elements and reset priority mode, so push() can be used in either mode again."""
        self._data=[]
        self._uses_priority=None
        self._counter=0

    def copy(self) -> "PriorityQueue[T]":
        """return a new, independent queue with the same contents and priority mode."""
        new:PriorityQueue[T]=PriorityQueue()
        new._data=list(self._data)
        new._uses_priority=self._uses_priority
        new._counter=self._counter
        return new


    def _priority(self,item:Tuple[Any,int,T]) -> Any:
        return item[0]

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
            try:
                if (self._data[i][0],self._data[i][1])<(self._data[p][0],self._data[p][1]):
                    self._swap(i,p)
                    i=p
                else:
                    break
            except TypeError:
                raise TypeError("values are not comparable for priority queue")

    def _heapify_down(self,i:int) -> None:
        """restore the heap property by sinking the item at index i downward."""
        size=len(self._data)
        while True:
            left=self._left(i)
            right=self._right(i)
            smallest=i
            try:
                if left<size and (self._data[left][0],self._data[left][1])<(self._data[smallest][0],self._data[smallest][1]):
                    smallest=left
                if right<size and (self._data[right][0],self._data[right][1])<(self._data[smallest][0],self._data[smallest][1]):
                    smallest=right
            except TypeError:
                raise TypeError("values are not comparable for priority queue")
            if smallest!=i:
                self._swap(i,smallest)
                i=smallest
            else:
                break