from collections import deque

from ..core.nodes import BinaryTreeNode as Node
from ..core.base_tree import TreeBase


class BinaryTree(TreeBase):
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