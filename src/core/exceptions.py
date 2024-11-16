class LayoutIndexError(IndexError):
    msg="index out of bounds. "
    def __init__(self, message=msg):
        super().__init__(message)

class LayoutAttributeError(AttributeError):
    msg="cannot modify attribute {}."
    def __init__(self, message=msg):
        super().__init__(message)