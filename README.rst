StructDC
========
.. image:: https://img.shields.io/pypi/v/structdc.svg
    :target: https://pypi.org/project/structdc/
    :alt: PyPI


Data class mapper for C structures

**Warning: alpha version, work in progress**

Install
-------
.. code:: python

    pip install structdc

Features
--------
* Supports packed and aligned structures
* Generates serialization and deserialization methods on data class creation

Example usage
-------------
.. code:: python

    from io import BytesIO
    from dataclasses import dataclass
    from structdc import StructMixin, Uint32, Uint64


    @dataclass
    class AlignedStruct(StructMixin):
        a: Uint32
        b: Uint64


    input = BytesIO(b'\xff\xff\xff\xff\x00\x00\x00\x00\xee\xee\xee\xee\xee\xee\xee\xee')
    decoded = AlignedStruct.from_bytestream(input)
    print(decoded)
    """
    AlignedStruct(a=4294967295, b=17216961135462248174)
    """


    @dataclass
    class PackedStruct(StructMixin, packed=True):
        a: Uint32
        b: Uint64

    input.seek(0)

    decoded = PackedStruct.from_bytestream(input)
    print(decoded)
    """
    PackedStruct(a=4294967295, b=17216961131453612032)
    """

    output = BytesIO(b'\x00' * 16)
    source_aligned = AlignedStruct(255, 65535)
    source_aligned.to_bytestream(output)
    output.seek(0)
    print(output.getvalue())
    """
    b'\xff\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00'
    """

    output = BytesIO(b'\x00' * 12)
    source_packed = PackedStruct(255, 65535)
    source_packed.to_bytestream(output)
    output.seek(0)
    print(output.getvalue())
    """
    b'\xff\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00'
    """

Coming soon
-----------
* Float numbers
* Strings and bytestrings
* Arrays
* Nested structures
