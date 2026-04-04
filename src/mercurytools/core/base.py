from .node import Node


class LinearBase:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size

    def __iter__(self):
        current=self._head
        while current:
            yield current.data
            current=current.next

    def __reversed__(self):
        current=self._tail
        while current:
            yield current.data
            current=current.prev

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"

    def __contains__(self,value):
        return any(item==value for item in self)

    def __eq__(self,other):
        if not isinstance(other,LinearBase):
            return False
        return list(self)==list(other)

    def __getitem__(self,index):
        if isinstance(index,slice):
            return self._slice(index)
        if index<0:
            index=self._size+index
        if index<0 or index>=self._size:
            raise IndexError("index out of bounds")

        return self._node_at(index).data


    def _slice(self,s: slice):
        start,stop,step=s.indices(self._size)
        result=self.__class__()
        i=0
        for item in self:
            if i>=start and i<stop and (i-start)%step==0:
                result._append_node(Node(item))
            i+=1
        return result

    def extend(self,iterable):
        for item in iterable:
            self._append_node(Node(item))

    def pop(self,index=-1):
        if self._size==0:
            raise IndexError("pop from empty structure")
        if index<0:
            index=self._size+index
        if index<0 or index>=self._size:
            raise IndexError("index out of bounds")
        node=self._node_at(index)
        return self._remove_node(node)

    def _node_at(self,index):
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
        self._head=None
        self._tail=None
        self._size=0

    def to_list(self):
        return list(self)

    def copy(self):
        new=self.__class__()
        for item in self:
            new._append_node(Node(item))
        return new

    def reverse(self):
        current=self._head
        self._head,self._tail=self._tail,self._head
        while current:
            current.next,current.prev=current.prev,current.next
            current=current.prev


    def _append_node(self,node:Node):
        if not self._head:
            self._head=self._tail=node
        else:
            node.prev=self._tail
            self._tail.next=node
            self._tail=node
        self._size+=1

    def _prepend_node(self,node:Node):
        if not self._head:
            self._head=self._tail=node
        else:
            node.next=self._head
            self._head.prev=node
            self._head=node
        self._size+=1

    def _remove_node(self,node:Node):
        if node.prev:
            node.prev.next=node.next
        else:
            self._head=node.next
        if node.next:
            node.next.prev=node.prev
        else:
            self._tail=node.prev
        self._size-=1
        return node.data