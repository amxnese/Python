try:
    print(int(77))
except ValueError:
    print("value error, please check the given input")
except ZeroDivisionError:
    print("can never divide by zero")
except NameError:
    print("there were some problems identifying")
except:
    print("something went wrong, please make sure that the given code is clean")
else:
    print("the code that has been writen is clean")
finally:
    print("all ways leads to rome")