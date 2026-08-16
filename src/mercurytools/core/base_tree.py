"""shared base class for binary tree structures [BinaryTree, BinarySearchTree, AVLTree]."""


from collections import deque

from .base import InternalStateGuard


class TreeBase(InternalStateGuard):
    """common state and traversal methods shared by all binary tree types."""
    _protected_fields=frozenset({"_root","_size"})

    def __init__(self):
        object.__setattr__(self,"_root",None)
        object.__setattr__(self,"_size",0)

    @property
    def size(self):
        """number of elements currently stored."""
        return self._size

    @property
    def root(self):
        """the root node, or None if the tree is empty."""
        return self._root
    
    def __contains__(self,value):
        """return True if value is present: O(n) here; 
        overridden with O(h) in ordered trees.
        """
        return any(item==value for item in self)

    def __iter__(self):
        """iterate over stored values in-order [left, node, right]: O(n) here; 
        overridden with O(h) in ordered trees.
        """
        return self.inorder()

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self.inorder())})"
    

    def inorder(self):
        """yield values in-order: left subtree, node, right subtree."""
        def _in(node):
            if node:
                yield from _in(node.left)
                yield node.data
                yield from _in(node.right)
        return _in(self._root)

    def preorder(self):
        """yield values pre-order: node, left subtree, right subtree."""
        def _pre(node):
            if node:
                yield node.data
                yield from _pre(node.left)
                yield from _pre(node.right)
        return _pre(self._root)

    def postorder(self):
        """yield values post-order: left subtree, right subtree, node."""
        def _post(node):
            if node:
                yield from _post(node.left)
                yield from _post(node.right)
                yield node.data
        return _post(self._root)
    
    def level_order(self):
        """yield values breadth-first, level by level, top to bottom."""
        if not self._root:
            return
        q=deque([self._root])
        while q:
            current=q.popleft()
            yield current.data
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    def min(self):
        """return the smallest value in the tree, or None if empty: O(n) here."""
        if self._size==0:
            return None
        return min(self)

    def max(self):
        """return the largest value in the tree, or None if empty: O(n) here."""
        if self._size==0:
            return None
        return max(self)

    def height(self):
        """return the tree's height 
        -- an empty tree has height -1, a single node has height 0: O(n) here; 
        overridden with O(h) in ordered trees.
        """
        def _height(node):
            if not node:
                return -1
            return 1+max(_height(node.left),_height(node.right))
        return _height(self._root)

    def clear(self):
        """remove all elements"""
        object.__setattr__(self,"_root",None)
        object.__setattr__(self,"_size",0)

    def _set_root(self,node):
        """set _root, bypassing the InternalStateGuard write-protection."""
        object.__setattr__(self,"_root",node)

    def _set_size(self,value):
        """set _size, bypassing the InternalStateGuard write-protection."""
        object.__setattr__(self,"_size",value)