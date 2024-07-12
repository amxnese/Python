MyGrades = {
    "math": "18",
    "physics": "17",
    "science": "16"
}
for grade in MyGrades:
    print(f"{grade} ==> {MyGrades[grade]}")
print(MyGrades)
print(MyGrades.items())

for grade_key, grade_value in MyGrades.items():
    print(f"{grade_key} ==> {grade_value}")