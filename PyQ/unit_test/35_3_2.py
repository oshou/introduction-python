import unittest


def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_15(self):
        self.assertEqual('FizzBuzz', fizzbuzz(15))

    def test_fizzbuzz_3(self):
        self.assertEqual('Fizz', fizzbuzz(3))

    def test_fizzbuzz_5(self):
        self.assertEqual('Buzz', fizzbuzz(5))

    def test_fizzbuzz_num(self):
        self.assertEqual('2', fizzbuzz(2))
