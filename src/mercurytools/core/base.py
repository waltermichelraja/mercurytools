class InternalStateGuard:
    _protected_fields=frozenset()

    def __setattr__(self,name,value):
        if name in self._protected_fields:
            raise AttributeError(f"'{name}' is read-only; mutate via the public API")
        object.__setattr__(self,name,value)