import unittest


def add_one(num):
    return num + 1


class TestAddOne(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(2, add_one(1))
