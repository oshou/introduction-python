def minus(a, b):
    if b > a:
        raise ValueError("b > a exception", a, b)
    return a - b


try:
    minus(8, 10)
except ValueError as e:
    print(e.args)
