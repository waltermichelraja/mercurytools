"""shared base class for doubly-linked sequential structures [LinkedList, Stack, Deque]."""


from .base import InternalStateGuard
from .nodes import LinearNode as Node
from .exceptions import EmptyStructureError,IndexOutOfBoundsError


class LinearBase(InternalStateGuard):
    """common state, iteration, indexing, and mutation helpers for linked sequences."""
    _protected_fields=frozenset({"_head","_tail","_size"})

    def __init__(self):
        object.__setattr__(self,"_head",None)
        object.__setattr__(self,"_tail",None)
        object.__setattr__(self,"_size",0)

    @property
    def head(self):
        """the first node in the structure, or None if empty."""
        return self._head
    
    @property
    def tail(self):
        """the last node in the structure, or None if empty."""
        return self._tail
    
    @property
    def size(self):
        """number of elements currently stored."""
        return self._size

    def __len__(self):
        return self._size

    def __iter__(self):
        """iterate over stored values from head to tail."""
        current=self._head
        while current:
            yield current.data
            current=current.next

    def __reversed__(self):
        """iterate over stored values from tail to head."""
        current=self._tail
        while current:
            yield current.data
            current=current.prev

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"

    def __contains__(self,value):
        """return True if value is present, using == comparison: O(n)."""
        return any(item==value for item in self)

    def __eq__(self,other):
        """two instances are equal if they hold the same values in the same order."""
        if not isinstance(other,LinearBase):
            return False
        return list(self)==list(other)

    def __getitem__(self,index):
        """return the value at index, or a new instance for a slice."""
        if isinstance(index,slice):
            return self._slice(index)
        if index<0:
            index=self._size+index
        if index<0 or index>=self._size:
            raise IndexOutOfBoundsError()
        return self._node_at(index).data


    def _slice(self,s: slice):
        """build a new instance of the same class from a slice of this one."""
        start,stop,step=s.indices(self._size)
        result=self.__class__()
        i=0
        for item in self:
            if i>=start and i<stop and (i-start)%step==0:
                result._append_node(Node(item))
            i+=1
        return result

    def extend(self,iterable):
        """append every item from iterable, in order, to the end: O(n)."""
        for item in iterable:
            self._append_node(Node(item))

    def pop(self,index=-1):
        """remove and return the value at index [default: the last element]."""
        if self._size==0:
            raise EmptyStructureError("pop from empty structure")
        if index<0:
            index=self._size+index
        if index<0 or index>=self._size:
            raise IndexOutOfBoundsError()
        node=self._node_at(index)
        return self._remove_node(node)

    def _node_at(self,index):
        """return the node at index, walking from whichever end is closer."""
        if index<self._size//2:
            current=self._head
            for _ in range(index):
                current=current.next
        else:
            current=self._tail
            for _ in range(self._size-index-1):
                current=current.prev
        return current


    def clear(self):
        """remove all elements."""
        object.__setattr__(self,"_head",None)
        object.__setattr__(self,"_tail",None)
        object.__setattr__(self,"_size",0)

    def to_list(self):
        """return the stored values as a plain Python list, head to tail."""
        return list(self)

    def copy(self):
        """return a new, independent instance with the same values in the same order."""
        new=self.__class__()
        for item in self:
            new._append_node(Node(item))
        return new

    def reverse(self):
        """reverse the structure in place. O(n), no new nodes allocated."""
        current=self._head
        object.__setattr__(self,"_head",self._tail)
        object.__setattr__(self,"_tail",current)
        while current:
            current.next,current.prev=current.prev,current.next
            current=current.prev

    def _set_size(self,value):
        """set _size, bypassing the InternalStateGuard write-protection."""
        object.__setattr__(self,"_size",value)


    def _append_node(self,node:Node):
        """attach node as the new tail: O(1)."""
        if not self._head:
            object.__setattr__(self,"_head",node)
            object.__setattr__(self,"_tail",node)
        else:
            node.prev=self._tail
            self._tail.next=node
            object.__setattr__(self,"_tail",node)
        self._set_size(self._size+1)

    def _prepend_node(self,node:Node):
        """attach node as the new head: O(1)."""
        if not self._head:
            object.__setattr__(self,"_head",node)
            object.__setattr__(self,"_tail",node)
        else:
            node.next=self._head
            self._head.prev=node
            object.__setattr__(self,"_head",node)
        self._set_size(self._size+1)

    def _remove_node(self,node:Node):
        """unlink node from the structure and return its data: O(1)."""
        if node.prev:
            node.prev.next=node.next
        else:
            object.__setattr__(self,"_head",node.next)
        if node.next:
            node.next.prev=node.prev
        else:
            object.__setattr__(self,"_tail",node.prev)
        self._set_size(self._size-1)
        return node.data