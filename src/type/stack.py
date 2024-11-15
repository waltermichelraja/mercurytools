from ..core.layout import Layout

class Stack(Layout):
    def __init__(self) -> None:
        super().__init__()
                
    def push(self, data) -> None:
        if super().Manager().is_node(data):
            data=data.data
        new_node=super().Node(data)
        new_node.index=self.length

        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev_node=self.tail
            self.tail.next_node=new_node
            self.tail=new_node
        self.length+=1
        return
    
    def pop(self):
        if self.head is None:
            raise IndexError("pop from an empty stack")
        pop_data=self.tail.data
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev_node
            self.tail.next_node=None
        self.length-=1
        return pop_data
