from typing import Union
from ._metatypes import *

__all__ = [
    'Uint8', 'Uint16', 'Uint16BE', 'Uint32', 'Uint32BE', 'Uint64', 'Uint64BE',
    'Int8', 'Int16', 'Int16BE', 'Int32', 'Int32BE', 'Int64', 'Int64BE'
]


class _Uint8(Integer, Bits8, Unsigned, LE):
    typing = Union['_Uint8', int]    


class _Uint16LE(Integer, Bits16, Unsigned, LE):
    typing = Union['_Uint16LE', int]


class _Uint16BE(Integer, Bits16, Unsigned, BE):
    typing = Union['_Uint16BE', int]


class _Uint32LE(Integer, Bits32, Unsigned, LE):
    typing = Union['_Uint32LE', int]


class _Uint32BE(Integer, Bits32, Unsigned, BE):
    typing = Union['_Uint32BE', int]


class _Uint64LE(Integer, Bits64, Unsigned, LE):
    typing = Union['_Uint64LE', int]


class _Uint64BE(Integer, Bits64, Unsigned, BE):
    typing = Union['_Uint64BE', int]


class _Int8(Integer, Bits8, Signed, LE):
    typing = Union['_Int8', int]


class _Int16LE(Integer, Bits16, Signed, LE):
    typing = Union['_Int16LE', int]


class _Int16BE(Integer, Bits16, Signed, BE):
    typing = Union['_Int16BE', int]


class _Int32LE(Integer, Bits32, Signed, LE):
    typing = Union['_Int32LE', int]


class _Int32BE(Integer, Bits32, Signed, BE):
    typing = Union['_Int32BE', int]


class _Int64LE(Integer, Bits64, Signed, LE):
    typing = Union['_Int64LE', int]


class _Int64BE(Integer, Bits64, Signed, BE):
    typing = Union['_Int64BE', int]


Uint8 = _Uint8.typing
Uint16 = _Uint16LE.typing
Uint16BE = _Uint16BE.typing
Uint32 = _Uint32LE.typing
Uint32BE = _Uint32BE.typing
Uint64 = _Uint64LE.typing
Uint64BE = _Uint64BE.typing
Int8 = _Int8.typing
Int16 = _Int16LE.typing
Int16BE = _Int16BE.typing
Int32 = _Int32LE.typing
Int32BE = _Int32BE.typing
Int64 = _Int64LE.typing
Int64BE = _Int64BE.typing

_type_mapping = {
    typeclass.typing: typeclass
    for typeclass in (
        _Uint8, _Uint16LE, _Uint16BE, _Uint32LE, _Uint32BE, _Uint64LE, _Uint64BE,
        _Int8, _Int16LE, _Int16BE, _Int32LE, _Int32BE, _Int64LE, _Int64BE
    )
}
