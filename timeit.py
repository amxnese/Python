import timeit
def test():
    """Stupid test function"""
    L = [i for i in range(100)]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))

list_test = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)
print(list_test,tuple_test)# import timeit
list_test = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)
print(list_test,tuple_test)