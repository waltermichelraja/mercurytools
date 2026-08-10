class MercuryError(Exception):
    pass


class EmptyStructureError(MercuryError,IndexError):
    def __init__(self,message="structure is empty"):
        super().__init__(message)


class IndexOutOfBoundsError(MercuryError,IndexError):
    def __init__(self,message="index out of bounds"):
        super().__init__(message)


class ValueNotFoundError(MercuryError,ValueError):
    def __init__(self,message="value not found"):
        super().__init__(message)