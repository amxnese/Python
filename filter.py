def checknum(num):
    if not num % 2:
        return True
nums = [4,63,6,48,86,12,42,7]
checknums = filter(checknum, nums)
print(list(checknums))

lst = list(map(lambda x:x*x,list(filter(lambda x:x%2==0,nums))))
print(lst)