from enum import Enum
from abc import ABC, abstractmethod
from typing import Type, Union

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
        # TODO: implement
        pass

    @classmethod
    def encoder(cls):
        # TODO: implement
        pass


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

