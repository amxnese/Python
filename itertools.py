import itertools
lst = [3,5,24,5,2]
x = itertools.accumulate(lst)
for i in x:
    print(i,end=' ')

lst1 = [1,2,3,4,5]
lst2 = ['A','B','C','D','E']
chain_lst = itertools.chain(lst1,lst2)
for i in chain_lst:
    print(i,end='')
  
x = [1,2,3]
y = ["one","two","three"]
z = [x,y]
ziped = [*(itertools.zip_longest(*t))]
print(ziped)


