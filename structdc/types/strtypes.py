from typing import Union, ByteString

from .abc import ByteField, RequiresConstraint
from .constraints import ByteConstraint, TextConstraint


class _BaseByteStringField(ByteField[bytes]):
    size: int
    __required_constraints__ = (ByteConstraint,)
    __stralign__: int

    def __init_subclass__(cls, constraint: ByteConstraint = ByteConstraint(0)):
        super().__init_subclass__(typing=Union[cls, ByteString])
        cls.size = constraint.size
        cls.__stralign__ = constraint.alignment

    @classmethod
    def decode_binary(cls, source: bytes) -> bytes:
        return source[:cls.__fieldsize__()] + \
               b'\x00' * (cls.__fieldsize__() - len(source) if len(source) < cls.__fieldsize__() else 0)

    @classmethod
    def encode_binary(cls, value: bytes) -> bytes:
        if len(value) > cls.__fieldsize__():
            raise ValueError(f'Value is too long({len(value)}) for field with size {cls.__fieldsize__()})')
        return bytes(value) + b'\x00' * (cls.__fieldsize__() - len(value))

    @classmethod
    def __fieldsize__(cls) -> int:
        return cls.size

    @classmethod
    def __alignment__(cls) -> int:
        return cls.__stralign__


class ByteStringField(RequiresConstraint, _BaseByteStringField):
    pass


class TextStringField(RequiresConstraint, _BaseByteStringField):
    encoding: str
    null_terminated: bool
    __required_constraints__ = (TextConstraint,)

    def __init_subclass__(cls, constraint: TextConstraint = TextConstraint(0)):
        super().__init_subclass__(constraint=constraint)
        cls.encoding = constraint.encoding
        cls.null_terminated = constraint.null_terminated

    @classmethod
    def encode_binary(cls, value: str) -> bytes:
        encoded = value.encode(cls.encoding)
        if len(encoded) > cls.__fieldsize__():
            raise ValueError(f'Encoded value is too long({len(encoded)}) for field with size {cls.__fieldsize__()})')
        return encoded + b'\x00' * (cls.__fieldsize__() - len(encoded))

    @classmethod
    def decode_binary(cls, source: bytes) -> str:
        decoded = (source[:cls.__fieldsize__()]
                   + b'\x00' * (cls.__fieldsize__() - len(source)
                                if len(source) < cls.__fieldsize__()
                                else 0)).decode(cls.encoding)
        return decoded.rstrip('\x00') if cls.null_terminated else decoded


__all__ = ['ByteStringField', 'TextStringField']
