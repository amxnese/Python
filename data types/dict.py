'sorting a dictionary'
dic = {}
for i in range(10,0,-1):
    dic[f"number{11-i}"] = i
sorted_dic = sorted(dic.items(),key=lambda x:x[1])
print(sorted_dic)

convert_net_speak = {
   "omg" : "oh my god",
   "lmao" : "laughing my ass off",
   "lol" : "laughing out loud"
}
print(convert_net_speak.get("lol"))

my_grades = {
    "math": "17",
    "physics": "16",
    "science": "16",
    "philosophy": "17"
}
for grade in mygrades:
    print (f"my grade in {grade} is {mygrades.get(grade)}")

    students = {
    "amine": {
        "math": "18",
        "physics": "17",
        "science": "16"
    },
    "khalil": {
        "math": "14",
        "physics": "13",
        "science": "12"
    },
    "hicham": {
        "math": "12",
        "physics": "13",
        "science": "11"
    }
    }
for name in students:
    print(f"{name} grades are:  ")
    for grades in students[name]:
        print(f"{grades}:  {students[name][grades]}")