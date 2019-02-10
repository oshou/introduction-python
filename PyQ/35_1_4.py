import unittest


def add_one(num):
    return num + 1


class TestAddOne(unittest.TestCase):
    def test_add_one(self):
        expected = 2
        actual = add_one(1)

        return self.assertEqual(expected, actual)
