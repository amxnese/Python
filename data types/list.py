lst = []
lst1 = [23,523,25,5,6]
lst2 = [42,2,62,1,4]
index1 = 0
index2 = 0
while len(lst1) > index1 and len(lst2) > index2:
    if lst1[index1] > lst2[index2]:
        lst.append(lst2[index2])
        index2 += 1
    else:
        lst.append(lst1[index1])
        index1 += 1
print(lst)

goals = (["money","success","respect"])
goals.append("inner_peace")
goals.insert(0,"wisdom")
goals.remove("money")
print(goals)