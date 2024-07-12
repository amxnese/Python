for i in range(0,11):
    if i%2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

for _ in range(0,25):
    print(0,end=',')

t = 92579702
for i in range(2000000000):
    if i == t:
        print(i)
        quit()