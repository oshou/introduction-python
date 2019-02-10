import unittest


def create_number_list(num):
    return list(range(num, num+10))


class TestCreateNumberList(unittest.TestCase):
    def test_create_number_list(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = create_number_list(1)

        self.assertEqual(expected, actual)
