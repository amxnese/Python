# Find E, Where E is Equivalent to:
'''
num = int
E = 1 * 1+2 * 1+2+3 * 1+2+3+4 * ... * 1+2+3+4+5+...+num
'''
while True:
    num = int(input("enter a number:  "))
    if num > 2:
        break
product = 1
numSum = 0
for i in range(1, num+1):
    numSum += i
    product *= numSum

# num = 4 ==> E = 1 * 3 * 6 * 10 = 180
print(f"Value of E: {product}")