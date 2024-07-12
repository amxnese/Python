MySkills = ["html", "css", "java", "python"]
MySkillsCounter = enumerate(MySkills, 1)
for a ,b in MySkillsCounter:
    print(f"{a} ==> {b}")

print(help(help))

list = ["amine", "steve", "son", "martin"]
list_counter = enumerate(list, 1)
for num, name in list_counter:
    print(f"{num + 0} ===> {name}")
r_list = reversed(list)
for r in r_list:
    print(r)