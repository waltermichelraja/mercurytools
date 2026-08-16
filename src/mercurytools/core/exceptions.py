"""custom exception hierarchy for mercurytools.
all exceptions raised by this library inherit from MercuryError.
"""


class MercuryError(Exception):
    """base class for all exceptions raised by mercurytools."""
    pass


class EmptyStructureError(MercuryError,IndexError):
    """raised when an operation requires at least one element but the structure is empty."""
    def __init__(self,message="structure is empty"):
        super().__init__(message)


class IndexOutOfBoundsError(MercuryError,IndexError):
    """raised when an index is outside the valid range for the structure."""
    def __init__(self,message="index out of bounds"):
        super().__init__(message)


class ValueNotFoundError(MercuryError,ValueError):
    """raised when a value expected to exist in the structure could not be found."""
    def __init__(self,message="value not found"):
        super().__init__(message)