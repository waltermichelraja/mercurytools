"""custom exception hierarchy for mercurytools.
all exceptions raised by this library inherit from MercuryError.
"""


from __future__ import annotations


class MercuryError(Exception):
    """base class for all exceptions raised by mercurytools."""
    pass


class EmptyStructureError(MercuryError,IndexError):
    """raised when an operation requires at least one element but the structure is empty."""
    def __init__(self,message:str="structure is empty") -> None:
        super().__init__(message)


class IndexOutOfBoundsError(MercuryError,IndexError):
    """raised when an index is outside the valid range for the structure."""
    def __init__(self,message:str="index out of bounds") -> None:
        super().__init__(message)


class ValueNotFoundError(MercuryError,ValueError):
    """raised when a value expected to exist in the structure could not be found."""
    def __init__(self,message:str="value not found") -> None:
        super().__init__(message)