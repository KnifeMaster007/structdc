from typing import Union, Tuple

from ._metaprogramming import annotation_parser
from .abc import ByteField
from structdc.types import const

__all__ = ['Float']


class Float(ByteField):
    __typing__ = Union['Float', float]
    endianess: const.Endianess = None

    @classmethod
    def decode_binary(cls) -> str:
        # TODO: implement
        pass

    @classmethod
    def encode_binary(cls) -> str:
        # TODO: implement
        pass


class BaseStruct(ByteField):
    __typing__ = Union['BaseStruct', object]

    @classmethod
    def decode_binary(cls, alignment=True) -> Tuple[str]:
        arguments = []
        offset = 0
        for _, field_type in annotation_parser(cls.__annotations__):
            align_offset = offset % field_type.__fieldsize__ if alignment else 0
            read_instruction = f'{const.bytes_var}.read({field_type.__fieldsize__ + align_offset})'
            if align_offset > 0:
                read_instruction += f'[{align_offset}:]'
            arguments.append(field_type.decode_binary().format(**{const.bytes_var: read_instruction}))
            offset += field_type.__fieldsize__
        return f'return cls({",".join(arguments)})',

    @classmethod
    def encode_binary(cls, alignment=True) -> Tuple[str]:
        arguments = []
        offset = 0
        for property_name, field_type in annotation_parser(cls.__annotations__):
            align_offset = offset % field_type.__fieldsize__ if alignment else 0
            if align_offset > 0:
                arguments.append(f"{const.bytes_var}.write(b'\\0' * {align_offset})")
            write_instruction = field_type.encode_binary().format(**{const.property_var: 'self.' + property_name})
            arguments.append(f"{const.bytes_var}.write({write_instruction})")
            offset += field_type.__fieldsize__
        return tuple(arguments)
