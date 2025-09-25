from ..core.layout_linear import LinearLayout

class LinkedList(LinearLayout):
    def __init__(self)->None:
        super().__init__()

    def append(self, data)->None:
        if super().Manager.is_node(data):
            data=data.data
        new_node=super().Node(data)
        new_node.index=self.length
        if not self.head:
            self.head=self.tail=new_node
        else:
            new_node.prev_node=self.tail
            self.tail.next_node=new_node
            self.tail=new_node
        self.length+=1

    def prepend(self, data)->None:
        if super().Manager.is_node(data):
            data=data.data
        new_node=super().Node(data)
        new_node.index=0
        if not self.head:
            self.head=self.tail=new_node
        else:
            new_node.next_node=self.head
            self.head.prev_node=new_node
            self.head=new_node
            super().Manager._update_indices_after_insert(new_node.next_node)
        self.length+=1

    def insert(self, data, index: int | None=None)->None:
        if index is None:
            index=self.length
        if index>self.length or index < 0:
            raise IndexError("index out of bounds")
        if super().Manager.is_node(data):
            data=data.data
        if index==self.length:
            self.append(data)
            return
        if index==0:
            self.prepend(data)
            return
        current=self.head
        while current and current.index < index:
            current=current.next_node
        new_node=super().Node(data)
        new_node.index=index
        new_node.prev_node=current.prev_node
        new_node.next_node=current
        if current.prev_node:
            current.prev_node.next_node=new_node
        current.prev_node=new_node
        super().Manager._update_indices_after_insert(new_node.next_node)
        self.length+=1

    def remove(self, data, start_index=0):
        if start_index<0 or start_index>=self.length:
            raise IndexError("index out of bounds")
        current=self.head
        i=0
        while current and i<start_index:
            current=current.next_node
            i+=1
        while current:
            if current.data==data:
                if current.prev_node:
                    current.prev_node.next_node=current.next_node
                else:
                    self.head=current.next_node
                if current.next_node:
                    current.next_node.prev_node=current.prev_node
                else:
                    self.tail=current.prev_node
                super().Manager._update_indices_after_remove(current.next_node)
                self.length-=1
                return current.data
            current=current.next_node
            i+=1
        raise ValueError(f"data: {data} not found")
