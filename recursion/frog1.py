ways = 1
minus = 1
def frog(feet):
    global ways
    global minus
    if feet == 0:
        return ways
        exit()
    else:
        ways += minus
        minus += 1
        return frog(feet-1)
print(frog(5))