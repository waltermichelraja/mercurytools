import inspect

class InternalStateGuard:
    _protected_fields=set()

    def __setattr__(self,name,value):
        if name in self._protected_fields:
            if hasattr(self,name):
                caller=inspect.currentframe().f_back.f_globals.get("__name__")
                if not (caller and caller.startswith("mercurytools")):
                    raise AttributeError(f"{name} is read-only")
        object.__setattr__(self,name,value)