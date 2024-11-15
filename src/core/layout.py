import inspect, sys
from .exceptions import *

class Layout:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.length=0
    
    def __setattr__(self, key, value):
        module = sys.modules[self.__module__]
        #core = sys.modules["mercury.src.core.layout"]
        currentframe=inspect.getmodule(inspect.currentframe().f_back)
        if module is not None and (module != currentframe):
            if key in self.__dict__:
                raise LayoutAttributeError(LayoutAttributeError.msg.format(key))
        super().__setattr__(key, value)

    def __getitem__(self, index) -> int:
        if not self.head or index >= self.length or index < -self.length:
            raise LayoutIndexError()
        if index >= 0:
            current = self.head
            while current and current.index < index:
                current = current.next_node
            if current and current.index == index:
                return current.data
        else:
            current = self.tail
            reverse_index = -1
            while current and reverse_index > index:
                current = current.prev_node
                reverse_index -= 1
            if current and reverse_index == index:
                return current.data
        raise LayoutIndexError()

    def __setitem__(self, index, value):
        if not self.head or index >= self.length or index < -self.length:
            raise LayoutIndexError()
        if index >= 0:
            current = self.head
            while current and current.index < index:
                current = current.next_node
            if current and current.index == index:
                current.data = value
                return
        else:
            current = self.tail
            reverse_index = -1
            while current and reverse_index > index:
                current = current.prev_node
                reverse_index -= 1
            if current and reverse_index == index:
                current.data = value
                return
        raise LayoutIndexError()
      
    def __repr__(self) -> str:
        nodes=[]
        current=self.head
        if not current:
            return "{0} < >".format(self.__class__.__name__)
        while current:
            if current.data==self: nodes.append("<...>"); current=current.next_node; continue
            nodes.append("{0}".format(current.data))
            current=current.next_node
        return "{0} < {1} >".format(self.__class__.__name__, " ; ".join(nodes))

    class Node():
        def __init__(self, data) -> None:
            self.data=data
            self.index=None
            self.next_node=None
            self.prev_node=None

        def __setattr__(self, key, value):
            currentmodule = sys.modules[self.__module__]
            currentframe = inspect.getmodule(inspect.currentframe().f_back)
            if currentmodule and currentframe:
                if (currentmodule.__name__==currentframe.__name__ or 
                    currentframe.__name__.startswith("mercury")):
                    super().__setattr__(key, value)
                else:
                    raise LayoutAttributeError(LayoutAttributeError.msg.format(key))
            else:
                raise LayoutAttributeError(LayoutAttributeError.msg.format(key))
            
        def __repr__(self) -> str:
            return "{0} < data: {1} >".format(self.__class__.__name__, self.data)

    class Manager:
        def __init__(self) -> None:
            pass

        def is_empty(self):
            return self.head is None
        
        def is_node(self, data):
            if type(data)==type(Layout.Node(data)):
                return True
            else:
                return False
        
        def __update_indices_after_remove(self, start_node):
            current = start_node
            while current:
                current.index -= 1
                current = current.next_node

        def __update_indices_after_insert(self, start_node):
            current = start_node
            while current:
                current.index += 1
                current = current.next_node

    def fetchindex(self, data) -> int:
        if not self.head:
            return 
        else:
            current=self.head
            while current:
                if current.data==data:
                    return current.index
                current=current.next_node
            return
        
"""    def fetchnode(self, index):
        if not self.head:
            return
        else:
            current=self.head
            while current.index==index:
                return current.data
            current=current.next_node
        return
"""

