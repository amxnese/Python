def factorial(num):
    if num == 0:
        return 1
    else:
        return (num * factorial(num-1))
print(factorial(5))

cache = {}
def fibonacci(index):
    if index in cache:
        return cache[index]
    elif index == 1 or index == 2:
        value = 1
        return value
    else:
        value = (fibonacci(index-1))+(fibonacci(index-2))
        if value not in cache:
            cache[index] = value
        return value

fib_cache = {}
def fib(n):
	if n in fib_cache:
		return fib_cache[n]
	elif n == 1 or n == 2:
		value = 1
		return value
	elif n > 2:
		value = fib(n-1) + fib(n-2)
		fib_cache[n] = value
		return value
for i in range(1,101):
		print(fib(i)) 

from functools import lru_cache
@lru_cache()
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(1,110):
    print(i,':',fibonacci(i))