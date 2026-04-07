from ..core.base_tree import TreeBase
from ..core.nodes import BinaryTreeNode as Node


class BinarySearchTree(TreeBase):
    def __repr__(self):
        return f"{self.__class__.__name__}({list(self.inorder())})"

    def __iter__(self):
        return self.inorder()

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

    def find(self,value):
        current=self._root
        while current:
            if value<current.data:
                current=current.left
            elif value>current.data:
                current=current.right
            else:
                return True
        return False

    def remove(self,value):
        self._root,deleted=self._remove(self._root,value)
        if deleted:
            self._size-=1
            return value
        raise ValueError(f"{value} not found")

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
        successor=self._min(node.right)
        node.data=successor.data
        node.right,_=self._remove(node.right,successor.data)
        return node,True

    def _min(self,node):
        while node.left:
            node=node.left
        return node


    def inorder(self):
        def _in(node):
            if node:
                yield from _in(node.left)
                yield node.data
                yield from _in(node.right)
        return _in(self._root)

    def preorder(self):
        def _pre(node):
            if node:
                yield node.data
                yield from _pre(node.left)
                yield from _pre(node.right)
        return _pre(self._root)

    def postorder(self):
        def _post(node):
            if node:
                yield from _post(node.left)
                yield from _post(node.right)
                yield node.data
        return _post(self._root)
