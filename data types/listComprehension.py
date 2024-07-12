'''    LIST COMPREHENSION    '''

def anagrams(word, words):
    for i in words:
        if sorted(i) == sorted(word):
            print(i)

def anagrams(word, words):
    return [i for i in words if sorted(i) == sorted(word)]

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))#, ['carer', 'racer'])
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))# => ['aabb', 'bbaa']
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])# => ['aabb', 'bbaa']

def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if type(i) is int]
print(filter_list([1, 2, "a", "b"]))

def flatten_the_curve(lst):
    if len(lst) == 0:
        return []
    return [round((sum(lst)/len(lst)),1)]*len(lst)

lst = [1,3,4,5,6]

lst1 = []
for i in lst:
    if i%2 == 0:
        lst1.append(i*i)
print(lst1)

lst2 = [i*i for i in lst if i%2 == 0]
print(lst2)

lst = [(i,n) for i in "abcd" for n in range(4)]
print(lst)

lst = []
for i in "abcd":
    for n in range(4):
        lst.append((i,n))
print(lst)

names = ['bruce','clark','logan','peter']
superhero = ['Batman','Superman','Wolverine','Spiderman']
print(list(zip(names,superhero)))

my_dict = {}
for name,hero in zip(names,superhero):
    my_dict[name] = hero
print(my_dict)
my_dict1 = {name:hero for name,hero in zip(names,superhero)if name != "peter"}
print(my_dict1)

def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])