"""unordered binary tree with level-order [complete-tree] insertion."""


from collections import deque

from ..core.nodes import BinaryTreeNode as Node
from ..core.base_tree import TreeBase


class BinaryTree(TreeBase):
    """a generic binary tree with no ordering guarantee between parent and children.
    insert() always fills the first available slot in level order 
    [i.e. keeps the tree "complete"].
    """

    def insert(self,data):
        """insert data into the first open slot found in level [breadth-first] order. O(n)."""
        new_node=Node(data)
        if not self._root:
            self._set_root(new_node)
            self._set_size(self._size+1)
            return
        q=deque([self._root])
        while q:
            current=q.popleft()
            if not current.left:
                current.left=new_node
                self._set_size(self._size+1)
                return
            else:
                q.append(current.left)
            if not current.right:
                current.right=new_node
                self._set_size(self._size+1)
                return
            else:
                q.append(current.right)