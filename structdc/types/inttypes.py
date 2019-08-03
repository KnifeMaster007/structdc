from typing import Union

from structdc.const import Endianess
from .abc import ByteField


class Integer(ByteField[int]):
    __typing__ = Union['Integer', int]
    signed: bool = None
    endianess: Endianess = None
    _value: int = None
    size: int

    def __init_subclass__(cls, size: int = 4, signed: bool = False,
                          endianess: Endianess = Endianess.PLATFORM):
        super().__init_subclass__(typing=Union[cls, int])
        cls.signed = signed
        cls.size = size
        cls.endianess = endianess

    @classmethod
    def decode_binary(cls, source: bytes) -> int:
        size = cls.__fieldsize__()
        if len(source) < size:
            raise ValueError(f'Source value shorter, than expected({size})')
        else:
            return int.from_bytes(source[:size], cls.endianess.value, signed=cls.signed)

    @classmethod
    def encode_binary(cls, value: int) -> bytes:
        return int.to_bytes(value, cls.__fieldsize__(), cls.endianess.value, signed=cls.signed)

    @classmethod
    def __fieldsize__(cls) -> int:
        return cls.size

    @classmethod
    def __alignment__(cls) -> int:
        return cls.__fieldsize__()


class _Uint8(Integer, size=1):
    pass


class _Uint16(Integer, size=2):
    pass


class _Uint16LE(Integer, size=2, endianess=Endianess.LITTLE):
    pass


class _Uint16BE(Integer, size=2, endianess=Endianess.BIG):
    pass


class _Uint32(Integer, size=4):
    pass


class _Uint32LE(Integer, size=4, endianess=Endianess.LITTLE):
    pass


class _Uint32BE(Integer, size=4, endianess=Endianess.BIG):
    pass


class _Uint64(Integer, size=8):
    pass


class _Uint64LE(Integer, size=8, endianess=Endianess.LITTLE):
    pass


class _Uint64BE(Integer, size=8, endianess=Endianess.BIG):
    pass


class _Int8(Integer, size=1, signed=True):
    pass


class _Int16(Integer, size=2, signed=True):
    pass


class _Int16LE(Integer, size=2, endianess=Endianess.LITTLE, signed=True):
    pass


class _Int16BE(Integer, size=2, endianess=Endianess.BIG, signed=True):
    pass


class _Int32(Integer, size=4, signed=True):
    pass


class _Int32LE(Integer, size=4, endianess=Endianess.LITTLE, signed=True):
    pass


class _Int32BE(Integer, size=4, endianess=Endianess.BIG, signed=True):
    pass


class _Int64(Integer, size=8, signed=True):
    pass


class _Int64LE(Integer, size=8, endianess=Endianess.LITTLE, signed=True):
    pass


class _Int64BE(Integer, size=8, endianess=Endianess.BIG, signed=True):
    pass


Uint8 = Union[_Uint8, int]
Uint16 = Union[_Uint16, int]
Uint16LE = Union[_Uint16LE, int]
Uint16BE = Union[_Uint16BE, int]
Uint32 = Union[_Uint32, int]
Uint32LE = Union[_Uint32LE]
Uint32BE = Union[_Uint32BE, int]
Uint64 = Union[_Uint64, int]
Uint64LE = Union[_Uint64LE, int]
Uint64BE = Union[_Uint64BE, int]
Int8 = Union[_Int8, int]
Int16 = Union[_Int16, int]
Int16LE = Union[_Int16LE, int]
Int16BE = Union[_Int16BE, int]
Int32 = Union[_Int32, int]
Int32LE = Union[_Int32LE]
Int32BE = Union[_Int32BE, int]
Int64 = Union[_Int64, int]
Int64LE = Union[_Int64LE, int]
Int64BE = Union[_Int64BE, int]


__all__ = [
    'Uint8',
    'Uint16',
    'Uint16LE',
    'Uint16BE',
    'Uint32',
    'Uint32LE',
    'Uint32BE',
    'Uint64',
    'Uint64LE',
    'Uint64BE',
    'Int8',
    'Int16',
    'Int16LE',
    'Int16BE',
    'Int32',
    'Int32LE',
    'Int32BE',
    'Int64',
    'Int64LE',
    'Int64BE'
]
