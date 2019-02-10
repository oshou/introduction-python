import unittest
from ext import find_extension


class TestFindExtention(unittest.TestCase):
    def test_existed(self):
        actual = find_extension('/path/to/test.py')
        expected = 'python'
        self.assertEqual(actual, expected)

    def test_not_exist(self):
        actual = find_extension('/path/to/test.js')
        expected = 'NONE'
        self.assertEqual(actual, expected)
