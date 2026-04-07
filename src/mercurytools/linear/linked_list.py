from ..core.base_linear import LinearBase
from ..core.nodes import LinearNode as Node
from ..core.exceptions import IndexOutOfBoundsError


class LinkedList(LinearBase):
    def append(self,data):
        self._append_node(Node(data))

    def prepend(self,data):
        self._prepend_node(Node(data))

    def insert(self,index,data):
        if index<0 or index>self._size:
            raise IndexOutOfBoundsError()
        if index==0:
            self.prepend(data)
            return
        if index==self._size:
            self.append(data)
            return
        current=self._head
        for _ in range(index):
            current=current.next
        node=Node(data)
        node.prev=current.prev
        node.next=current
        current.prev.next=node
        current.prev=node
        self._size+=1

    def remove(self,value):
        current=self._head
        while current:
            if current.data==value:
                return self._remove_node(current)
            current=current.next
        raise ValueError(f"{value} not found")