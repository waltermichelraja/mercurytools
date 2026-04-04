class MercuryError(Exception):
    pass


class EmptyStructureError(MercuryError):
    def __init__(self,message="structure is empty"):
        super().__init__(message)


class IndexOutOfBoundsError(MercuryError):
    def __init__(self,message="index out of bounds"):
        super().__init__(message)