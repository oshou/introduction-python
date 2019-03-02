import unittest
import math


class TestPow(unittest.TestCase):
    def test_pow(self):
        actual = math.pow(4, 2)
        expected = 16
        self.assertEqual(actual, expected)

    def test_negative(self):
        actual = math.pow(4, -2)
        expected = 0.0625
        self.assertEqual(actual, expected)


class TestCeil(unittest.TestCase):
    def test_float(self):
        actual = math.ceil(4.8)
        expected = 5
        self.assertEqual(actual, expected)

    def test_int(self):
        actual = math.ceil(2)
        expected = 2
        self.assertEqual(actual, expected)


class TestFactorial(unittest.TestCase):
    def test_int(self):
        actual = math.factorial(8)
        expected = 40320
        self.assertEqual(actual, expected)

    def test_negative(self):
        with self.assertRaises(ValueError):
            math.factorial(-8)
