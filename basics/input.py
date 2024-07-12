a = input("enter a number:   ")
b = input("enter a number:   ")
c = input("enter a number:   ")
if a>b and b>c:
    print(a,b,c)
elif a>b and c>b:
    print(a,c,b)
elif b>a and a>c:
    print(b,a,c)
elif b>c and c>a:
    print(b,c,a)
elif c>b and b>a:
    print(c,b,a)
else:
    print(c,a,b)