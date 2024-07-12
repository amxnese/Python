utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup","fork"}
utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes)
print(utensils)
print(dishes)
print(dinner_table)
print(utensils.intersection(dishes))