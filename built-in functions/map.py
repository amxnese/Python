MyList = ["amine","harry","fury","mohamed"]

def formattxt(text):
    return (f"- {text} -")

def say_hi(name):
    return (f"hello {name} its nice seeing you here ")

# map With a Defined Function
myformattxt = map(formattxt,MyList)

welcome = map(say_hi, MyList)
for line in welcome:
    print(line)

# map With lambda
for line in map(lambda text : f"- { text} -",MyList):
    print(line)

items = [
    ("product1", 15),
    ("product3", 12),
    ("product2", 41)
]
# Storing The Second Elements of The Tuples in The List in a New List

# Regular Solution
lst = []
for item in items:
    lst.append(item[1])

# Using a map
lst1 = list(map(lambda item: item[1],items))
print(lst1)