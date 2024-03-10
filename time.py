import time

for seconds in range(10,0,-1):
  print(seconds)
  time.sleep(1)
print("happy birthday")

def decorator(fun):
  def speed_test():
    start = time.time() 
    fun()
    end = time.time()
    print(f"time token to run your function is:  {end - start}")
  return speed_test

from string import digits
from itertools import product
start = time() 
for x in product(digits,repeat=4):
    print(*x)
end = time()
print(f"time token to run your function is:  {end - start}")

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        x = func()
        total = time.time() - start
        print("Time: ",total)
    return wrapper()
@timer
def test():
    for i in range(100000000):
        pass

from random import randint
password = 123456789
given = 0000
start = time()
while given != password:
    given = randint(0,999999999)
for i in range(999999999):
    if i == password:
        given = i
        break
end = time()
print(given)
print(end-start)
