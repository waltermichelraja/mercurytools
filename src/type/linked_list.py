from ..core.layout_linear import LinearLayout

class LinkedList(LinearLayout):
    def __init__(self)->None:
        super().__init__()
        
    def append(self, data)->None:
        if super().Manager().is_node(data):
            data=data.data
        new_node=super().Node(data)
        new_node.index=self.length
        if self.head is None:
            self.head=self.tail=new_node
        else:
            new_node.prev_node=self.tail
            self.tail.next_node=new_node
            self.tail=new_node
        self.length+=1
        return

    def prepend(self, data)->None:
        if super().Manager().is_node(data):
            data=data.data
        new_node=super().Node(data)
        new_node.index=0

        if self.head is None:
            self.head=self.tail=new_node
        else:
            new_node.next_node=self.head
            self.head.prev_node=new_node
            self.head=new_node
        super().Manager()._update_indices_after_insert(new_node.next_node)
        self.length+=1
        return

    def insert(self, data, index=None)->None:
        if index is not None and index > self.length:
            raise IndexError("index out of bounds")
        if index is None:
            index=self.length
        if super().Manager().is_node(data):
            data=data.data
        new_node=super().Node(data)
        new_node.index=index
        if self.head is None:
            self.head=self.tail=new_node
        elif index==self.length:
            self.append(data)
            return
        elif index==0:
            self.prepend(data)
            return
        else:
            current=self.head
            while current and current.index < index:
                current=current.next_node
            new_node.prev_node=current.prev_node
            new_node.next_node=current
            if current.prev_node:
                current.prev_node.next_node=new_node
            current.prev_node=new_node
            if index==0:
                self.head=new_node
            super().Manager()._update_indices_after_insert(new_node.next_node)
        self.length+=1
        return

    def remove(self, data, start_index=0):
        if start_index<0 or start_index>=self.length:
            raise IndexError("index out of bounds")
        current=self.head
        length=0
        while current and length<start_index:
            current=current.next_node
            length+=1
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
                super().Manager()._update_indices_after_remove(current.next_node)
                self.length-=1
                return current.data
            current=current.next_node
            length+=1
        return None
