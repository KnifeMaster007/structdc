from enum import Enum


bytes_input_var = '_in_bytes'
property_input_var = '_in_property'


class Endianess(Enum):
    LITTLE = 'little'
    BIG = 'big'
