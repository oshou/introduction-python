import unittest
from main import get_none, get_num, get_list, raise_value_error


class TestGetNone(unittest.TestCase):
    def test_get(self):
        self.assertIsNone(get_none())


class TestGetNum(unittest.TestCase):
    def test_get(self):
        actual = get_num()
        self.assertGreaterEqual(actual, 0)
        self.assertLess(actual, 10)


class TestGetList(unittest.TestCase):
    def test_get(self):
        actual = get_list()
        self.assertEqual(len(actual), 5)
        self.assertIn(0, actual)
        self.assertLess(set(actual), {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})


class TestRaiseValueError(unittest.TestCase):
    def test_raise(self):
        with self.assertRaises(ValueError):
            raise_value_error()
