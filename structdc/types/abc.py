from abc import ABC, abstractmethod
from typing import Union, Type, Generic, TypeVar, Sequence
from dataclasses import Field


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
    def encode_binary(cls, value: T) -> bytes:
        pass

    @classmethod
    @abstractmethod
    def __fieldsize__(cls) -> int:
        pass

    @classmethod
    @abstractmethod
    def __alignment__(cls) -> int:
        pass


class CTypeConstraint(ABC):
    pass


class RequiresConstraint:
    __required_constraints__: Sequence[CTypeConstraint]


class ConstraintedField(Field):
    __ctype_constraint__: CTypeConstraint

    def __init__(self, ctype_constraint, default, default_factory, init, repr, hash, compare, metadata):
        super().__init__(default, default_factory, init, repr, hash, compare, metadata)
        self.__ctype_constraint__ = ctype_constraint


__all__ = [ByteField]
