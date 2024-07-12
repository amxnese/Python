def frog(feet):
    ways = 1
    minus = 1
    multi = 0
    if feet == 1:
        minus += 1
        ways += (multi-minus)*minus
        if minus == feet:
            return ways
        else:
            return(frog(feet-minus))
    multi += 1
    return(frog(feet-minus))
print(frog(4))