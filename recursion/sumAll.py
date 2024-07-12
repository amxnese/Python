def sum_all(n):
    if n == 0:
        return 1
    else:
        return sum_all(n-1) + sum_all(n-2)
print(sum_all(5))