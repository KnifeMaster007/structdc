from typing import Union

from .abc import ByteField


def annotation_parser(annotations):
    for property_name, field in annotations.items():
        if getattr(field, '__origin__', None) is not Union:
            raise ValueError(f'Property "{property_name}" type "{field} is unsupported"')
        try:
            field_type = next(i for i in field.__args__ if issubclass(i, ByteField))
        except StopIteration:
            raise ValueError(f'Property "{property_name}" type "{field} is unsupported"')
        yield property_name, field_type
