from functools import reduce
def sum(num1, num2):
    return num1 + num2
NumList = [1,2,3,4,5]
result = reduce(sum,NumList)
print(result)

factorial = [5,4,3,2,1]
def fact(num1,num2):
    return num1*num2
result = reduce(fact,factorial)
print(result)

