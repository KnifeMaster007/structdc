from ..const import Endianess


class BE:
    endianess = Endianess.BIG


class LE:
    endianess = Endianess.LITTLE


class Signed:
    signed = True


class Unsigned:
    signed = False


class Bits8:
    size = 1


class Bits16:
    size = 2


class Bits32:
    size = 4


class Bits64:
    size = 8


__all__ = [Bits64, Bits32, Bits16, Bits8, Signed, Unsigned, BE, LE]
