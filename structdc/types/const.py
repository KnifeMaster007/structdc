import sys
from enum import Enum


bytes_var = '__bytes'
property_var = '__property'


class Endianess(Enum):
    LITTLE = 'little'
    BIG = 'big'
    PLATFORM = sys.byteorder
