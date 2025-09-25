import inspect, sys
from .exceptions import *


class LinearLayout:
    def __init__(self)->None:
        self.head: "LinearLayout.Node | None"=None
        self.tail: "LinearLayout.Node | None"=None
        self.length: int=0

    def __setattr__(self, key, value):
        if key in self.__dict__:
            caller=inspect.getmodule(inspect.currentframe().f_back)
            if caller and caller.__name__!=self.__module__:
                raise LayoutAttributeError(LayoutAttributeError.msg.format(key))
        super().__setattr__(key, value)

    def __getitem__(self, index: int):
        if not self.head or index>=self.length or index < -self.length:
            raise LayoutIndexError()
        current=self.head if index>=0 else self.tail
        i=0 if index>=0 else -1
        while current:
            if i==index:
                return current.data
            current=current.next_node if index>=0 else current.prev_node
            i=i+1 if index>=0 else i-1
        raise LayoutIndexError()

    def __setitem__(self, index: int, value):
        if not self.head or index>=self.length or index < -self.length:
            raise LayoutIndexError()
        current=self.head if index>=0 else self.tail
        i=0 if index>=0 else -1
        while current:
            if i==index:
                current.data=value
                return
            current=current.next_node if index>=0 else current.prev_node
            i=i+1 if index>=0 else i-1
        raise LayoutIndexError()
      
    def __repr__(self)->str:
        nodes=[]
        current=self.head
        if not current:
            return "{0} < >".format(self.__class__.__name__)
        while current:
            if current.data==self: nodes.append("<...>"); current=current.next_node; continue
            nodes.append("{0}".format(current.data))
            current=current.next_node
        return "{0} < {1} >".format(self.__class__.__name__, " ; ".join(nodes))

    class Node:
        def __init__(self, data)->None:
            self.data=data
            self.index: int | None=None
            self.next_node: "LinearLayout.Node | None"=None
            self.prev_node: "LinearLayout.Node | None"=None

        def __setattr__(self, key, value):
            if key=="data":
                super().__setattr__(key, value)
                return
            caller=inspect.getmodule(inspect.currentframe().f_back)
            if caller and (caller.__name__==self.__module__ or caller.__name__.startswith("mercury")):
                super().__setattr__(key, value)
            else:
                raise LayoutAttributeError(LayoutAttributeError.msg.format(key))

        def __repr__(self)->str:
            return f"{self.__class__.__name__} < data: {self.data} >"

    class Manager:
        @staticmethod
        def is_empty(layout: "LinearLayout")->bool:
            return layout.head is None

        @staticmethod
        def is_node(data)->bool:
            return isinstance(data, LinearLayout.Node)

        @staticmethod
        def _update_indices_after_remove(start_node: "LinearLayout.Node | None")->None:
            current=start_node
            while current:
                current.index-=1
                current=current.next_node

        @staticmethod
        def _update_indices_after_insert(start_node: "LinearLayout.Node | None")->None:
            current=start_node
            while current:
                current.index+=1
                current=current.next_node

    def index(self, data)->int | None:
        current=self.head
        while current:
            if current.data==data:
                return current.index
            current=current.next_node
        return None

    def node(self, index: int)->"Node | None":
        current=self.head
        while current:
            if current.index==index:
                return current
            current=current.next_node
        return None
