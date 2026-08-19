"""write-protection guard used by LinearBase and TreeBase.
blocks assignment to any name listed in a subclass's _protected_fields
from anywhere except the base class's own object.__setattr__ calls
[see LinearBase/TreeBase's _set_* helpers].
"""


from __future__ import annotations
from typing import Any, ClassVar, FrozenSet


class InternalStateGuard:
    _protected_fields:ClassVar[FrozenSet[str]]=frozenset()

    def __setattr__(self,name:str,value:Any) -> None:
        if name in self._protected_fields:
            raise AttributeError(f"'{name}' is read-only; mutate via the public API")
        object.__setattr__(self,name,value)