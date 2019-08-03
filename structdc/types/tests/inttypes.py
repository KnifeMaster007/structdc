import unittest

import structdc.types.inttypes as inttypes
from structdc.const import Endianess
from typing import Union


class TestInteger(unittest.TestCase):
    def test_decode_binary(self):
        for size in (1, 2, 4, 8):
            for _, endianess in Endianess.__members__.items():
                for signed in (True, False):
                    raw_bytes = b'\xff' * size
                    testval = int.from_bytes(raw_bytes, endianess.value, signed=signed)
                    testclass = type('TestInt', (inttypes.Integer,), {})
                    testclass.endianess = endianess
                    testclass.signed = signed
                    testclass.size = size
                    self.assertEqual(testval, testclass.decode_binary(raw_bytes))
                    self.assertRaises(ValueError, lambda: testclass.decode_binary(raw_bytes[:-1]))

    def test_encode_binary(self):
        for size in (1, 2, 4, 8):
            for _, endianess in Endianess.__members__.items():
                for signed in (True, False):
                    raw_bytes = b'\xff' * size
                    testval = int.from_bytes(raw_bytes, endianess.value, signed=signed)
                    testclass = type('TestInt', (inttypes.Integer,), {})
                    testclass.endianess = endianess
                    testclass.signed = signed
                    testclass.size = size
                    self.assertEqual(raw_bytes, testclass.encode_binary(testval))

    def test_alignment_equals_size(self):
        for size in (1, 2, 4, 8):
            testclass = type('TestInt', (inttypes.Integer,), {})
            testclass.size = size
            self.assertEqual(size, testclass.__alignment__())

    def test_type_aliases_validity(self):
        for power in range(1, 4):
            size = 2 ** power
            bittness = size * 8
            suffixes = {Endianess.LITTLE: 'LE', Endianess.BIG: 'BE', Endianess.PLATFORM: ''}
            for endianess, suffix in suffixes.items():
                for signed in (True, False):
                    prefix = 'I' if signed else 'Ui'
                    typing = getattr(inttypes, f'{prefix}nt{bittness}{suffix}')
                    self.assertIs(typing.__origin__, Union)
                    origins = list(filter(lambda it: issubclass(it, inttypes.Integer), typing.__args__))
                    self.assertEqual(1, len(origins))
                    self.assertTrue(issubclass(origins[0], inttypes.Integer))
                    self.assertEqual(origins[0].size, size)
                    self.assertEqual(origins[0].endianess, endianess)
                    self.assertEqual(origins[0].signed, signed)
