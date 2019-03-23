from enum import Enum
from abc import ABC, abstractmethod
from typing import Type, Union
from .._meta.const import bytes_input_var, property_input_var

__all__ = ['BE', 'LE', 'Signed', 'Unsigned', 'Bits8', 'Bits16', 'Bits32',
           'Bits64', 'Integer']


class _Endianess(Enum):
    LITTLE = 'little'
    BIG = 'big'


class _ByteField(ABC):
    size: int = None
    typing: Type = Union['_ByteField', bytes]

    @classmethod
    @abstractmethod
    def decoder(cls) -> str:
        pass

    @classmethod
    @abstractmethod
    def encoder(cls) -> str:
        pass


class Integer(_ByteField):
    typing = Union['Integer', int]
    signed: bool = None
    endianess: _Endianess = None

    @classmethod
    def decoder(cls):
        return f'int.from_bytes(bytes={{{bytes_input_var}}}, ' \
               f'byteorder={cls.endianess.value}, signed={cls.signed})'

    @classmethod
    def encoder(cls):
        return f'int.to_bytes(self={{{property_input_var}}}, length={cls.size}, ' \
               f'byteorder={cls.endianess.value}, signed={cls.signed})'


class Float(_ByteField):
    typing = Union['Float', float]
    endianess: _Endianess = None

    @classmethod
    def decoder(cls) -> str:
        # TODO: implement
        pass

    @classmethod
    def encoder(cls) -> str:
        # TODO: implement
        pass


class BE:
    endianess = _Endianess.BIG


class LE:
    endianess = _Endianess.LITTLE


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

