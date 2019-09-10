from typing import Any
from functools import reduce
from collections import OrderedDict

from structdc.types.abc import ByteField


class StructField:
    __field__: ByteField
    __offset__: int

    def __init__(self, field: ByteField, offset: int):
        self.__field__ = field
        self.__offset__ = offset


class Structure(ByteField[Any]):
    __structfields__: OrderedDict

    @classmethod
    def decode_binary(cls, source: bytes) -> 'Structure':
        pass

    @classmethod
    def encode_binary(cls, value: 'Structure') -> bytes:
        pass

    @classmethod
    def __fieldsize__(cls) -> int:
        reduce(lambda acc, it: )    # FIXME
        # FIXME

    @classmethod
    def __alignment__(cls) -> int:
        return reduce(lambda acc, it: it.__field__.__alignment__() if it.__field__.__alignment__ > acc else acc,
                      cls.__structfields__.values(), 1)
