from io import BytesIO
from structdc.types.metatypes import BaseStruct
from ..const import bytes_var


class StructMixin(BaseStruct):
    def __init_subclass__(cls, packed=False, **kwargs):
        decode_method = f"@classmethod\ndef from_bytestream(cls, {bytes_var}: BytesIO):\n" + \
                        ' \n'.join([' ' * 4 + line for line in cls.decode_binary(not packed)])
        encode_method = f"def to_bytestream(self, {bytes_var}: BytesIO):\n" + \
                        ' \n'.join([' ' * 4 + line for line in cls.encode_binary(not packed)])
        namespace = {}
        cls.__structalignment__ = not packed
        exec(decode_method, globals(), namespace)
        exec(encode_method, globals(), namespace)
        cls.from_bytestream = namespace['from_bytestream']
        cls.to_bytestream = namespace['to_bytestream']

    @classmethod
    def from_bytestream(cls, bytestream: BytesIO) -> 'StructMixin':
        pass

    def to_bytestream(self, bytestream: BytesIO):
        pass
