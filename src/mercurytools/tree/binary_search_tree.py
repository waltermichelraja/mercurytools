from ..core.base_tree import TreeBase
from ..core.nodes import BinaryTreeNode as Node


class BinarySearchTree(TreeBase):
    def __contains__(self,value):
        current=self._root
        while current:
            if value<current.data:
                current=current.left
            elif value>current.data:
                current=current.right
            else:
                return True
        return False


    def _remove(self,node,value):
        if not node:
            return node,False
        if value<node.data:
            node.left,deleted=self._remove(node.left,value)
            return node,deleted
        if value>node.data:
            node.right,deleted=self._remove(node.right,value)
            return node,deleted
        if not node.left and not node.right:
            return None,True
        if not node.left:
            return node.right,True
        if not node.right:
            return node.left,True
        successor=self._min_node(node.right)
        node.data=successor.data
        node.right,_=self._remove(node.right,successor.data)
        return node,True

    def _min_node(self,node):
        while node.left:
            node=node.left
        return node


    def insert(self,data):
        if not self._root:
            self._root=Node(data)
            self._size+=1
            return
        current=self._root
        while True:
            if data<current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=Node(data)
                    self._size+=1
                    return
            elif data>current.data:
                if current.right:
                    current=current.right
                else:
                    current.right=Node(data)
                    self._size+=1
                    return
            else:
                return

    def remove(self,value):
        self._root,deleted=self._remove(self._root,value)
        if deleted:
            self._size-=1
            return value
        raise ValueError(f"{value} not found")

    def min(self):
        if not self._root:
            return None
        node=self._root
        while node.left:
            node=node.left
        return node.data

    def max(self):
        if not self._root:
            return None
        node=self._root
        while node.right:
            node=node.right
        return node.data