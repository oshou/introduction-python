import unittest


def plus(a, b):
    return a + b


class TestPlus(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(10, plus(2, 8))
