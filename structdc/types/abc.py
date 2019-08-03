from abc import ABC, abstractmethod
from typing import Union, Type, Any, Generic, TypeVar


T = TypeVar('T')


class ByteField(ABC, Generic[T]):
    __typing__: Type = Union['ByteField', bytes]

    def __init_subclass__(cls, typing=Union['ByteField', bytes]):
        cls.__typing__ = typing

    @classmethod
    @abstractmethod
    def decode_binary(cls, source: bytes) -> T:
        pass

    @classmethod
    @abstractmethod
    def encode_binary(self, value: T) -> bytes:
        pass

    @classmethod
    @abstractmethod
    def __fieldsize__(cls) -> int:
        pass

    @classmethod
    @abstractmethod
    def __alignment__(cls) -> int:
        pass


__all__ = [ByteField]
