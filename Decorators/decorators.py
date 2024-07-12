def Decorator(fun):
  def nested(*nums):
    for num in nums:
      if num < 0:
        print("Beware! there is at least one number less than zero")
    fun(*nums)
  return nested
def Decorator1(fun):
  def nested1(*nums):
    print("saying hello from  the second decorator")
    fun(*nums)
  return nested1
@Decorator
@Decorator1
def add(num1, num2, num3):
  print(num1 + num2 + num3)
add(22,4, -55)


@Decorator
def bignum():
  for i in range(1, 20000):
    print(i)
bignum()