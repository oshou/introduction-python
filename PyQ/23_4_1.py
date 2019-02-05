def fib(n):
    if n == 1:
        ans = 0
    elif n == 2:
        ans = 1
    else:
        ans = fib(n-1) + fib(n-2)


print(fib(10))
