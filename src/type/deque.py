from ..core.layout import Layout

class Deque(Layout):
    def __init__(self) -> None:
        super().__init__()

    def append(self, data) -> None:
        if super().Manager().is_node(data):
            data=data.data
        new_node=super().Node(data)
        new_node.index=self.length

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node=self.tail
            self.tail.next_node=new_node
            self.tail=new_node
        self.length+=1
        del new_node
        return
    
    def prepend(self, data) -> None:
        if super().Manager().is_node(data):
            data=data.data
        new_node=super().Node(data)
        new_node.index=0

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        super().Manager()._Manager__update_indices_after_insert(new_node.next_node)
        self.length+=1
        del new_node
        return

    def pop_head(self) -> None:
        if self.head is None:
            raise IndexError("pop from an empty deque")
        
        pop_data=self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
        super().Manager()._Manager__update_indices_after_remove(self.head)
        self.length-=1
        return pop_data

    def pop_tail(self) -> None:
        if self.head is None:
            raise IndexError("pop from an empty deque")
        
        pop_data=self.tail.data
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev_node
            self.tail.next_node=None
        self.length-=1
        return pop_data
    