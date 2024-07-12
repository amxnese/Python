x = [1,2,3,4,5,6,7,8,9]
z = (1,2,3,4,5,6,7,8,9)
from sys import getsizeof
print(getsizeof(x))
print(getsizeof(z))

from sys import exit
list = [3,3,4,2,2,5,6]
if 3 in list:
    print("found")
    exit(0)
print("not found")
exit(1)

import sys
def iter(n):
    for i in range(n):
        yield i
lst = [i for i in range(100000)]
g = iter(100000)
print(sys.getsizeof(lst))
print(sys.getsizeof(g))