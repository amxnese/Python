list1 = [1,2,3,4,5]
list2 = ["A","B","C"]
tuple1 = ("woman", "man","girl", "boy")
dict1 = {"amine": 20 ,"harry": 32,"terry":5}
ultimateList = zip(list1,list2,list3)
for item in ultimateList:
    print(item)
for item1, item2,item3,item4 in zip(list1, list2, tuple1, dict1):
    print("List 1 item ==>", item1)
    print("List 2 item ==>", item2)
    print("tuple 1 item ==>", item3)
    print("dict1 key ==>", item4, ", dict1 value ==>", dict1[item4])