from typing import Union

from ._metaprogramming import annotation_parser
from .abc import ByteField
from .. import const

__all__ = ['Integer', 'Float']


class Integer(ByteField):
    typing = Union['Integer', int]
    signed: bool = None
    endianess: const.Endianess = None

    @classmethod
    def __rawdecoder__(cls):
        return f'int.from_bytes(bytes={{{const.bytes_var}}}, ' \
               f'byteorder=\'{cls.endianess.value}\', signed={cls.signed})'

    @classmethod
    def __rawencoder__(cls):
        return f'int.to_bytes({{{const.property_var}}}, length={cls.size}, ' \
               f'byteorder=\'{cls.endianess.value}\', signed={cls.signed})'


class Float(ByteField):
    typing = Union['Float', float]
    endianess: const.Endianess = None

    @classmethod
    def __rawdecoder__(cls) -> str:
        # TODO: implement
        pass

    @classmethod
    def __rawencoder__(cls) -> str:
        # TODO: implement
        pass


class BaseStruct(ByteField):
    typing = Union['BaseStruct', object]
    __structalignment__ = True

    @classmethod
    def __rawdecoder__(cls) -> str:
        arguments = []
        offset = 0
        for _, field_type in annotation_parser(cls.__annotations__):
            align_offset = offset % field_type.size if cls.__structalignment__ else 0
            read_instruction = f'{const.bytes_var}.read({field_type.size + align_offset})'
            if align_offset > 0:
                read_instruction += f'[{align_offset}:]'
            arguments.append(field_type.__rawdecoder__().format(**{const.bytes_var: read_instruction}))
            offset += field_type.size
        return f'cls({",".join(arguments)})'

    @classmethod
    def __rawencoder__(cls) -> str:
        arguments = []
        offset = 0
        for property_name, field_type in annotation_parser(cls.__annotations__):
            align_offset = offset % field_type.size if cls.__structalignment__ else 0
            if align_offset > 0:
                arguments.append(f"{const.bytes_var}.write(b'\\0' * {align_offset})")
            write_instruction = field_type.__rawencoder__().format(**{const.property_var: 'self.' + property_name})
            arguments.append(f"{const.bytes_var}.write({write_instruction})")
            offset += field_type.size
        return "\n".join(arguments) + '\n'
