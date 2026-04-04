class Node:
    __slots__=("data","next","prev")

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

    def __repr__(self):
        return f"Node({self.data})"