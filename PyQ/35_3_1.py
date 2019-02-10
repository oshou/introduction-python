import unittest


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


class TestLeapYear(unittest.TestCase):
    def test_is_not_leap_year_(self):
        return self.assertEqual(False, is_leap_year(2013))

    def test_is_leap_year_4(self):
        return self.assertEqual(True, is_leap_year(4))

    def test_is_leap_year_100(self):
        return self.assertEqual(False, is_leap_year(100))

    def test_is_leap_year_400(self):
        return self.assertEqual(True, is_leap_year(400))
