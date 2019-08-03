import unittest

from ..strtypes import *
from ..constraints import *


class TestStrTypes(unittest.TestCase):
    size = 255
    align = 2

    def test_bytestring(self):
        testbs = type('testbs', (ByteStringField,), {})
        self.assertIn(ByteConstraint, testbs.__required_constraints__)
        testbs.__init_subclass__(constraint=ByteConstraint(self.size, self.align))
        self.assertEqual(self.size, testbs.__fieldsize__())
        self.assertEqual(self.align, testbs.__alignment__())
        test_bytes = b'\xb0\xb5'
        self.assertEqual(test_bytes + b'\x00' * (self.size - len(test_bytes)), testbs.encode_binary(test_bytes))
        self.assertRaises(ValueError, lambda: testbs.encode_binary(test_bytes * (self.size + 1)))
        self.assertEqual(test_bytes + b'\x00' * (self.size - len(test_bytes)), testbs.decode_binary(test_bytes))
        self.assertEqual(test_bytes + b'\x00' * (self.size - len(test_bytes)),
                         testbs.decode_binary(test_bytes + b'\x00' * self.size))

    def test_textstring(self):
        testts = type('testts', (TextStringField,), {})
        self.assertIn(TextConstraint, testts.__required_constraints__)
        testts.__init_subclass__(constraint=TextConstraint(self.size, self.align, 'utf8', null_terminated=False))
        self.assertEqual(self.size, testts.__fieldsize__())
        self.assertEqual(self.align, testts.__alignment__())
        test_str = u'Съешь еще этих мягких французских булок'
        encoded_str = test_str.encode('utf8')
        padded_test_str = (encoded_str + b'\x00' * (self.size - len(encoded_str))).decode('utf8')
        self.assertEqual(encoded_str + b'\x00' * (self.size - len(encoded_str)), testts.encode_binary(test_str))
        self.assertRaises(ValueError, lambda: testts.encode_binary(test_str + u'P' * self.size))
        self.assertEqual(padded_test_str, testts.decode_binary(encoded_str))
        self.assertEqual(padded_test_str, testts.decode_binary(encoded_str + b'\x00' * (self.size - len(encoded_str))))
        testts.__init_subclass__(constraint=TextConstraint(self.size, self.align, 'utf8', null_terminated=True))
        self.assertEqual(test_str, testts.decode_binary(encoded_str))
        self.assertEqual(test_str, testts.decode_binary(encoded_str + b'\x00' * (self.size - len(encoded_str))))
