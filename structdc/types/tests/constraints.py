import unittest

from ..constraints import *


class TestConstraints(unittest.TestCase):
    size = 255
    align = 2
    encoding = 'utf8'

    def test_byteconstraint(self):
        self.assertRaises(ValueError, lambda: ByteConstraint(-1))
        self.assertRaises(ValueError, lambda: ByteConstraint(0, 0))
        testc = ByteConstraint(self.size, self.align)
        self.assertEqual((testc.size, testc.alignment), (self.size, self.align))

    def test_textconstraint(self):
        testc = TextConstraint(self.size, self.align, self.encoding)
        self.assertEqual(testc.encoding, self.encoding)
