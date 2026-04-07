from collections import deque

from .base import InternalStateGuard


class TreeBase(InternalStateGuard):
    _protected_fields={"_root","_size"}
    def __init__(self):
        self._root=None
        self._size=0

    @property
    def size(self):
        return self._size

    @property
    def root(self):
        return self._root
    
    def __contains__(self,value):
        return any(item==value for item in self)

    def __iter__(self):
        return self.inorder()

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self.inorder())})"
    

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
            return
        q=deque([self._root])
        while q:
            current=q.popleft()
            yield current.data
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)


    def height(self):
        def _height(node):
            if not node:
                return -1
            return 1+max(_height(node.left),_height(node.right))
        return _height(self._root)

    def clear(self):
        self._root=None
        self._size=0