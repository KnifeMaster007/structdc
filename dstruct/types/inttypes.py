from typing import Union

from .metatypes import Integer
from ._mixins import LE, BE, Unsigned, Signed, Bits8, Bits16, Bits32, Bits64

__all__ = [
    'Uint8', 'Uint16', 'Uint16BE', 'Uint32', 'Uint32BE', 'Uint64', 'Uint64BE'
]


class _Uint8(Bits8, Unsigned, LE, Integer):
    typing = Union['_Uint8', int]    


class _Uint16LE(Bits16, Unsigned, LE, Integer):
    typing = Union['_Uint16LE', int]


class _Uint16BE(Bits16, Unsigned, BE, Integer):
    typing = Union['_Uint16BE', int]


class _Uint32LE(Bits32, Unsigned, LE, Integer):
    typing = Union['_Uint32LE', int]


class _Uint32BE(Bits32, Unsigned, BE, Integer):
    typing = Union['_Uint32BE', int]


class _Uint64LE(Bits64, Unsigned, LE, Integer):
    typing = Union['_Uint64LE', int]


class _Uint64BE(Bits64, Unsigned, BE, Integer):
    typing = Union['_Uint64BE', int]


class _Int8(Bits8, Signed, LE, Integer):
    typing = Union['_Int8', int]


class _Int16LE(Bits16, Signed, LE, Integer):
    typing = Union['_Int16LE', int]


class _Int16BE(Bits16, Signed, BE, Integer):
    typing = Union['_Int16BE', int]


class _Int32LE(Bits32, Signed, LE, Integer):
    typing = Union['_Int32LE', int]


class _Int32BE(Bits32, Signed, BE, Integer):
    typing = Union['_Int32BE', int]


class _Int64LE(Bits64, Signed, LE, Integer):
    typing = Union['_Int64LE', int]


class _Int64BE(Bits64, Signed, BE, Integer):
    typing = Union['_Int64BE', int]


Uint8 = Union[_Uint8, int]
Uint16 = Union[_Uint16LE, int]
Uint16BE = Union[_Uint16BE, int]
Uint32 = Union[_Uint32LE, int]
Uint32BE = Union[_Uint32BE, int]
Uint64 = Union[_Uint64LE, int]
Uint64BE = Union[_Uint64BE, int]
Int8 = Union[_Int8, int]
Int16 = Union[_Int16LE, int]
Int16BE = Union[_Int16BE, int]
Int32 = Union[_Int32LE, int]
Int32BE = Union[_Int32BE, int]
Int64 = Union[_Int64LE, int]
Int64BE = Union[_Int64BE, int]
