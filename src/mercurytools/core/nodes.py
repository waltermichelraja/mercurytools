class LinearNode:
    __slots__=("data","next","prev")

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"


class LRUNode:
    __slots__=("key","value","prev","next")

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key}:{self.value})"


class BinaryTreeNode:
    __slots__=("data","left","right","height")

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"
