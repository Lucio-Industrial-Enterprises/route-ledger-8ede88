import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_valid_quantity(self):
        self.assertEqual(parse_quantity("  5  "), 5)

    def test_zero(self):
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_large_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-100")
