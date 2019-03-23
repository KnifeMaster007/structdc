from abc import ABC, abstractmethod
from typing import Union, Type


class ByteField(ABC):
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


__all__ = [ByteField]
