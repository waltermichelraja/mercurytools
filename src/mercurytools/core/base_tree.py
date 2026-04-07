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

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self._size})"


    def clear(self):
        self._root=None
        self._size=0