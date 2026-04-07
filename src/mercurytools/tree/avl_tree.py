from ..core.base_tree import TreeBase
from ..core.nodes import BinaryTreeNode as Node


class AVLTree(TreeBase):
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

    def insert(self,data):
        self._root=self._insert(self._root,data)

    def _insert(self,node,data):
        if not node:
            self._size+=1
            return Node(data)
        if data<node.data:
            node.left=self._insert(node.left,data)
        elif data>node.data:
            node.right=self._insert(node.right,data)
        else:
            return node
        self._update_height(node)
        return self._rebalance(node,data)

    def remove(self,value):
        self._root,deleted=self._remove(self._root,value)
        if deleted:
            self._size-=1
            return value
        raise ValueError(f"{value} not found")

    def _remove(self,node,value):
        if not node:
            return None,False
        if value<node.data:
            node.left,deleted=self._remove(node.left,value)
        elif value>node.data:
            node.right,deleted=self._remove(node.right,value)
        else:
            if not node.left:
                return node.right,True
            if not node.right:
                return node.left,True
            successor=self._min_node(node.right)
            node.data=successor.data
            node.right,deleted=self._remove(node.right,successor.data)
        self._update_height(node)
        return self._rebalance_after_delete(node),deleted

    def _min_node(self,node):
        while node.left:
            node=node.left
        return node


    def _height(self,node):
        return node.height if node else 0

    def _balance(self,node):
        return self._height(node.left)-self._height(node.right)

    def _update_height(self,node):
        node.height=1+max(self._height(node.left),self._height(node.right))

    def _rebalance(self,node,data):
        balance=self._balance(node)
        if balance>1 and data<node.left.data:
            return self._rotate_right(node)
        if balance<-1 and data>node.right.data:
            return self._rotate_left(node)
        if balance>1 and data>node.left.data:
            node.left=self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance<-1 and data<node.right.data:
            node.right=self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rebalance_after_delete(self,node):
        balance=self._balance(node)
        if balance>1 and self._balance(node.left)>=0:
            return self._rotate_right(node)
        if balance>1 and self._balance(node.left)<0:
            node.left=self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance<-1 and self._balance(node.right)<=0:
            return self._rotate_left(node)
        if balance<-1 and self._balance(node.right)>0:
            node.right=self._rotate_right(node.right)
            return self._rotate_left(node)
        return node


    def _rotate_left(self,z):
        y=z.right
        T2=y.left
        y.left=z
        z.right=T2
        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_right(self,z):
        y=z.left
        T3=y.right
        y.right=z
        z.left=T3
        self._update_height(z)
        self._update_height(y)
        return y
    
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