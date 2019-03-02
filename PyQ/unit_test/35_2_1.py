import unittest


def is_even(num):
    return num % 2 == 0


class TestEven(unittest.TestCase):
    def test_is_even_2(self):
        self.assertEqual(True, is_even(2))

    def test_is_even_3(self):
        self.assertEqual(False, is_even(3))
