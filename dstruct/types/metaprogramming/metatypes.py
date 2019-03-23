from .abc import ByteField
from typing import Union
from dstruct.types.metaprogramming import const

__all__ = ['Integer', 'Float']


class Integer(ByteField):
    typing = Union['Integer', int]
    signed: bool = None
    endianess: const.Endianess = None

    @classmethod
    def decoder(cls):
        return f'int.from_bytes(bytes={{{const.bytes_input_var}}}, ' \
               f'byteorder=\'{cls.endianess.value}\', signed={cls.signed})'

    @classmethod
    def encoder(cls):
        return f'int.to_bytes({{{const.property_input_var}}}, length={cls.size}, ' \
               f'byteorder=\'{cls.endianess.value}\', signed={cls.signed})'


class Float(ByteField):
    typing = Union['Float', float]
    endianess: const.Endianess = None

    @classmethod
    def decoder(cls) -> str:
        # TODO: implement
        pass

    @classmethod
    def encoder(cls) -> str:
        # TODO: implement
        pass
