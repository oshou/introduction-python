import random


def get_none():
    return None


def get_num():
    return random.randint(0, 9)


def get_list():
    candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return [random.choice(candidates) for _ in range(4)] + [0]


def raise_value_error():
    raise ValueError
