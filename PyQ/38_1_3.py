import sys
import os


class MyClass(object):
    def echo_osname(self):
        return "{}({})".format(os.name, sys.platform)


def sum_numbers(numbers):
    # comment
    summary = 0
    for num in numbers:
        summary = summary + num
    return summary


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sum_numbers(numbers))
print(MyClass().echo_osname())
