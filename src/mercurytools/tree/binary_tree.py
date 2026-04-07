from ..core.nodes import BinaryTreeNode as Node
from ..core.base_tree import TreeBase
from collections import deque


class BinaryTree(TreeBase):
    def __repr__(self):
        return f"{self.__class__.__name__}({list(self.level_order())})"

    def insert(self,data):
        new_node=Node(data)
        if not self._root:
            self._root=new_node
            self._size+=1
            return
        q=deque([self._root])
        while q:
            current=q.popleft()
            if not current.left:
                current.left=new_node
                self._size+=1
                return
            else:
                q.append(current.left)
            if not current.right:
                current.right=new_node
                self._size+=1
                return
            else:
                q.append(current.right)


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

    def level_order(self):
        if not self._root:
            return iter([])
        q=deque([self._root])
        while q:
            current=q.popleft()
            yield current.data
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)


    def find(self,value):
        return any(item==value for item in self.level_order())

    def height(self):
        def _height(node):
            if not node:
                return -1
            return 1+max(_height(node.left),_height(node.right))
        return _height(self._root)