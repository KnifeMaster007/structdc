from typing import Union

from .abc import ByteField


def annotation_parser(dataclass_fields):
    for property_name, field in dataclass_fields.items():
        if getattr(field.type, '__origin__', None) is not Union:
            raise ValueError(f'Property "{field.name}" type "{field.type} is unsupported"')
        try:
            field_type = next(i for i in field.type.__args__ if issubclass(i, ByteField))
        except StopIteration:
            raise ValueError(f'Property "{field.name}" type "{field.type} is unsupported"')
        yield property_name, field_type

