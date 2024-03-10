'sorting a dictionary'
dic = {}
for i in range(10,0,-1):
    dic[f"number{11-i}"] = i
sorted_dic = sorted(dic.items(),key=lambda x:x[1])
print(sorted_dic)