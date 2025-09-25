from ..core.layout_linear import LinearLayout

class Stack(LinearLayout):
    def __init__(self)->None:
        super().__init__()

    def push(self, data)->None:
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

    def pop(self):
        if not self.head:
            raise IndexError("pop from an empty stack")
        pop_data=self.tail.data
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            old_tail=self.tail
            self.tail=self.tail.prev_node
            self.tail.next_node=None
            super().Manager._update_indices_after_remove(self.tail.next_node)
        self.length-=1
        return pop_data
