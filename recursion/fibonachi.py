def fib(x):
    if x > 2:
        return fib(x-1) + fib(x-2)
    else:
        return 1
print(fib(3))