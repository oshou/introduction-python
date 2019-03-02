import unittest


class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('FOO', 'foo'.upper())

    def test_not_upper(self):
        self.assertNotEqual('foo', 'foo'.upper())

    def test_is_digit(self):
        self.assertTrue('123'.isdigit())

    def test_is_not_digit(self):
        self.assertFalse('123ppap'.isdigit())
