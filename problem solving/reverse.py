def Reverse( s ):
    result = ""
    n = 0
    start = 0
    while ( s[n:] != "" ):
        while ( s[n:] != "" and s[n] != ' ' ):
            n += 1
            result = s[ start: n ] + " " + result
            start = n
    return result

def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]
print(rreverse("hello"))

def rrr(s):
    if  len(s) < 2:
      return s
    else:
      return rrr(s[1:]) + s[0]
print(rrr("amine"))