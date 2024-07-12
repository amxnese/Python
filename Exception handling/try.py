try:
    value = int(input("enter a number:  "))
    print(value)
    result = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError as err1:
    print(err1)
print("success")

try:
    number = int(input("enter a number:   "))
    print("the given input is an integer from try ")
except:
    print("the given input is not an integer ")
else:
    print("the given input is an integer from else")
finally:
    print("this line  will appear no matter what")