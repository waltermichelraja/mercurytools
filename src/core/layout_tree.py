import inspect, sys
from .exceptions import *

class TreeLayout:
    def __init__(self) -> None:
        self.root=None
        self.size=0

    def __setattr__(self, key, value):
        module = sys.modules[self.__module__]
        #core = sys.modules["mercury.src.core.layout"]
        currentframe=inspect.getmodule(inspect.currentframe().f_back)
        if module is not None and (module != currentframe):
            if key in self.__dict__:
                raise LayoutAttributeError(LayoutAttributeError.msg.format(key))
        super().__setattr__(key, value)

    def __getitem__(self, index) -> int:
        if not self.head or index >= self.size or index < -self.size:
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
        if not self.head or index >= self.size or index < -self.size:
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

    class Node:
        def __init__(self, data) -> None:
            self.data=data
            self.index=None
            self.parent=None
            self.child=None

        def __setattr__(self, key, value):
            currentmodule = sys.modules[self.__module__]
            currentframe = inspect.getmodule(inspect.currentframe().f_back)
            if key=="data":
                super().__setattr__(key, value)
                return
            if currentmodule and currentframe:
                if (currentmodule.__name__==currentframe.__name__ or 
                    currentframe.__name__.startswith("mercury")):
                    super().__setattr__(key, value)
                else:
                    raise LayoutAttributeError(LayoutAttributeError.msg.format(key))
            else:
                raise LayoutAttributeError(LayoutAttributeError.msg.format(key))

    class Manager:
        def __init__(self):
            pass
        
        def is_empty(self):
            return self.root is None
        
        def is_node(self, data):
            if type(data)==type(TreeLayout.Node(data)):
                return True
            else:
                return False
