import re

my_search = re.search(r"\w{3}","amine5")
print(my_search.span())
print(my_search.string)
print(my_search.group())
print(my_search)
is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@@osama.com")
if is_email:
    print("the input given is a valid email")
else:
    print("validation denied")

email_given = input("please enter your email:  ")
search = re.findall("[A-z0-9\.]+@[A-z0-9]+\.(com|net)",email_given)
list = []
if search != []:
    list.append(email_given)
    print("email succesfully added to the list")
    print(list)
else:
    print("input given has not been considered as an email")

x = "i love the programing language named python"
print(y)
string = "how-to-write_a_very-good-article"
for i,d in enumerate(stringed):
    if len(d) < 2:
        continue
    else:
        print(f"word number : {i+1} ==> {d}")

import os
print("="*50)
print(os.getcwd())
print("="*50)

import re
x = "just wanted it to feel more practical"
z = re.sub("\s","...",x)
print(z)

my_web = ("https://www.elzero.org:8080/category.php?article=105?name=how-to-do")
my_search = search("(https?)://(www)?\.?(\w+)\.(\w+):(\d+)?/?(.+)",my_web)
print(my_search)
print(dir(my_search))
print(my_search.group())
print(my_search.groups())
for group in my_search.groups():
    print(group) 
