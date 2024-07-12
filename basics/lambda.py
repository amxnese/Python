age = lambda age : age[1] >= 18
agechecking = list(filter(age, buddies))
for line in agechecking:
    print(line)

friends =["amine", "cris", "micheal", "fred", "alfred"]
for friend in filter(lambda name : name.startswith("a"), friends):
    print(friend)

lst = [[4,2],[2,6],[1,5],[3,9]]
lst.sort(key=lambda x:x[1])
print(lst)