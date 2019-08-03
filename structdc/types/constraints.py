from .abc import CTypeConstraint


class ByteConstraint(CTypeConstraint):
    size: int
    alignment: int

    def __init__(self, size: int, alignment: int = 1):
        if size < 0 or alignment < 1:
            raise ValueError
        else:
            self.size = size
            self.alignment = alignment


class TextConstraint(ByteConstraint):
    encoding: str
    null_terminated: bool

    def __init__(self, size: int, alignment: int = 1, encoding: str = 'ascii', null_terminated=True):
        super().__init__(size, alignment)
        self.encoding = encoding
        self.null_terminated = null_terminated


__all__ = ['ByteConstraint', 'TextConstraint']
