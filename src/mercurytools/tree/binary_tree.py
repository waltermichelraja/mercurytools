from collections import deque


class _Node:
    __slots__=("data","left","right")

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __repr__(self):
        return f"Node({self.data})"


class BinaryTree:
    def __init__(self):
        self._root=None
        self._size=0

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"BinaryTree({list(self.level_order())})"

    def __setattr__(self,name,value):
        if name in {"_root","_size"}:
            if name in self.__dict__:
                import inspect
                caller=inspect.stack()[1].frame.f_globals.get("__name__")
                if caller!=__name__:
                    raise AttributeError(f"{name} is read-only")
        super().__setattr__(name,value)

    @property
    def size(self):
        return self._size

    @property
    def root(self):
        return self._root


    def insert(self,data):
        new_node=_Node(data)
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
        for item in self.level_order():
            if item==value:
                return True
        return False

    def height(self):
        def _height(node):
            if not node:
                return -1
            return 1+max(_height(node.left),_height(node.right))
        return _height(self._root)

    def clear(self):
        self._root=None
        self._size=0