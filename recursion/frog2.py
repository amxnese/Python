ways = 1
def frog(feet):
    global ways
    minus = 1
    if minus == feet:
        return ways
        exit()
    else:
        ways = ways + (feet-minus)*minus

        return frog(feet-minus)
print(frog(4))