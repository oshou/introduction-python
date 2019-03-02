import unittest
from user import User


class TestUser(unittest.TestCase):
    def test_fullname(self):
        user = User('Tarou', 'Suzuki', '')
        actual = user.fullname()
        expected = 'Tarou Suzuki'
        self.assertEqual(actual, expected)

    def test_roll_staff(self):
        user = User('Tarou', 'Suzuki', 'tarou@my-company.com')
        actual = user.role()
        expected = 'staff'
        self.assertEqual(actual, expected)

    def test_roll_viewer(self):
        user = User('Jirou', 'Suzuki', 'jirou@gmail.com')
        actual = user.role()
        expected = 'viewer'
        self.assertEqual(actual, expected)
