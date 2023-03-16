# name = 'amine'
# print(name*10)
# x = 4
# y = 8
# z = '5'

# print(x+5)
# print(y+8)
# print(x*y)

# name = input("what's your name?:   ")
# print("hello"+" "+(name))
# age = float(input("how old are you?:    "))
# age = age + 1
# print("wow" + " " + str(age) + " " + "you're pretty mature")
# height = input("how tall are you?:   ")
# print("you can't be " + (height) + " mm")
# # import math
# x = 5
# y = 8
# z = 25
# pi = 3.14
# print(pow(y,5454))
# print(math.sqrt(z))
# print(max(x,y,z))
# print(min(x,y,z))
# name = "amine sedrata"
# first_name = name[0:5]
# last_name = name[6:13]
# funky_name = name[0:13:2]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funky_name)0=
# print(reversed_name)

# school = "larbi ben mhidi high school"
# slice = slice(0,-12)
# print(school[slice])

# age = int(input("how old are you?:   "))
# if age >= 100:
#   print("you can't be")
# elif age > 18:
#    print("you are an adult")
# elif age < 0:
#    print("you haven't been born yet")
# else:
#    print("you're such a baby")

# temp = int(input("what's the temperature outside?:    "))
# if temp >= 0 and temp <= 30:
#    print("the temperature is good today ")
#    print("you can go outside")

# while 1==1:
#    print("help i'm stuck in a loop")
# name = ""
# while len(name) == 0:
#    name = input("enter your name")
# print("hello "+name)
# name = None
# while not name:
#    name = input("enter your name:   ")
# print("hello "+name)

# for i in range(50):
#    print(i)
# for me in "amine":
#    print(me)

# import time
# for me in range(0,10,-1)
#   print(me)
#    time.sleep(1)
# print("happy new year")
# import time

# for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)
# print("happy birthday")

# def cube(num):
#    return num*num*num
# print(cube(5))

# def say_hi(name):
#    print("hello "+name)
# say_hi("bro")

# color1 = input("enter a color:  ")
# color2 = input("enter a second color:  ")
# print("roses are "+color1)
# print("violets are "+color2)

# goals = (["money","success","respect"])
# goals.append("inner_peace")
# goals.insert(0,"wisdom")
# goals.remove("money")
# print(goals)

# ages = [3,5,8,1,0,8,66,44,32,15,85,39,8,667,34,32,17,95]
# ages.sort()
# print(ages)
# from typing import List

# names1 = ["amine", "mohamed", "alex", "jake"]

# names2 = names1.copy()
# names1.append(1)
# print(names2)
# print(names1)

# def welcome(name,age):
#    print("hello " + name + " you are " + age + " years old")
# welcome("amine","20")

# def cube(num):
#    return num*num*num
# def sum(num1,num2):
#    return num1+num2
# print(sum(55,77))

# is_tired = False
# wants_to_work = False
# if is_tired and wants_to_work:
#    print("you should rest \nyour safety comes first")
# elif wants_to_work and not is_tired:
#    print("go bust your ass")
# elif is_tired:
#    print("get some rest")
# elif not is_tired and not wants_to_work:
#    print("you deserve a a day off")
# else:
#    print("go to work")

# print(max(53,87,53))

# def match_string(str1, str2):
#    if str1 == str2:
#        print("the strings do match")
#    else:
#        print("the strings do not match")
# match_string("good morning", "good evening")

# num1 = float(input("enter a number:  "))
# operator = input("enter an operator :  ")
# num2 = float(input("enter a number:  "))
# if operator == "+":
#    print(num1+num2)
# elif operator == "-":
#    print(num1-num2)
# elif operator == "*":
#    print(num1*num2)
# elif operator == "/":
#    print(num1/num2)
# else:
#    print("something went wrong! please try again")

# convert_net_speak = {
#    "omg" : "oh my god",
#    "lmao" : "laughing my ass off",
#    "lol" : "laughing out loud"
# }
# print(convert_net_speak.get("lol"))

# i = 0
# while i <= 50:
#    i += 5
#    if i == 25:
#        continue
#    elif i == 35:
#        print("reached a forbidden number")
#        break
#    print(i)
# else:
#    print("the condition is not true anymore")

# languages = ["java_script","python","java","c#","c++"]
# for x in languages:
#    print(x)

# for x in range(30,46):
#    print(x)

# for x in range(10):
#    if x % 2 == 0:
#        print(x, " is an even number")
#    else:
#        print(x, " is an odd number")

# for x in range(len(languages)):
#    if languages[x] == "python":
#        print(x,(" is the one"))
#        break
#    elif languages[x] != "python":
#        print(x," is not the one")
# else:
#    print(x, " not found")

# for x in languages:
#    if x == "python":
#        print(x,(" is the one"))
#        break
# else:
#   print("the one is not found")

# def power(num1, num2):
#    result = 1
#    for x in range(num2):
#        result = result * num2
#    return result
# print(power(5,30))

# no_list = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [0]
# ]
# for x in no_list:
#    for y in x:
#        print(y*(y+1))

# try:
#    value = int(input("enter a number:  "))
#    print(value)
#    result = 10 / 0
# except ZeroDivisionError as err:
#    print(err)
# except ValueError as err1:
#    print(err1)
# print("success")

# cm_in_meter = 100
# meter_in_km = 1000
# the_shield = ["roman reigns", "dean ambrose", "seth rollins"]

# rows = int(input("how many rows?:   "))
# columns = int(input("how many columns?:   "))
# symbol = input("enter a symbol:   ")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# student = ("bro",21,"male")
# print(student.count("bro"))
# print(student.index("male"))
# for x in student:
#     print(x)
# if "bro" in student:
#     print("bro is here")

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup","fork"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)
# print(utensils)
# print(dishes)
# print(dinner_table)
# print(utensils.intersection(dishes))

# capitals = {'America':'washington dc',
#             'Algeria':'algiers',
#             'France':'paris',
#             'Russia':'moscow'}

# admins = ["Amine","Khalil","Sadek","Rafik","Mahmoud"]
# name = input("please enter your name:   ").capitalize().strip()
# if name in admins:
#     print(f"hello {name} WELCOME back")
#     option = input("would you like to update or delete your name?   ").capitalize().strip()
#     while not option == "Delete" and not option == "Update":
#         option = input("something went wrong, please try again\nwould you like to delete or update your name?:   ").capitalize().strip()
#     if option == "Delete":
#         admins.remove(name)
#         print(f"name ({name}) has been deleted")
#     elif option == "Update":
#         NewName = input("please enter your new name:  ").capitalize().strip()
#         admins[admins.index(name)] = NewName
#         print("name updated successfully")
# else:
#     print(f"hello {name} this is your first time here")
#     status = input("would you like to be an admin? (yes or no):    ").strip().capitalize()
#     while not status == "Yes" and not status == "No":
#         status = input("something went wrong, please try again\nwould you like to be an admin? (yes or no):    ").capitalize().strip()
#     if status == "Yes":
#         admins.append(name)
#         print("you are an admin now")
#     elif status == "No":
#         print("you will be signed in as a guest ")

# MyFavoriteWebsites = []
# MaximumWebs = 5
# while MaximumWebs > 0:
#     web = input("enter the website name without https://:     ")
#     MyFavoriteWebsites.append(f"https://{web.lower().strip()}")
#     print(MyFavoriteWebsites)
#     MaximumWebs -= 1
#     print(f"website added\n{MaximumWebs} places left")
# else:
#     print("bookmark is full, can't add more")
# if len(MyFavoriteWebsites) > 0:
#     MyFavoriteWebsites.sort()
#     index = 0
#     print("printing the list of websites in your bookmark")
#     while index < len(MyFavoriteWebsites):
#         print(MyFavoriteWebsites[index])
#         index += 1
#
# tries = 4
# mainPassword = "amine123"
# givenPassword = input("enter your password:   ")
# while not givenPassword == mainPassword:
#     tries -= 1
#     if tries == 1:
#         print("careful, this is your last chance")
#         givenPassword = input("enter your password:   ")
#     elif tries > 0:
#         print(f"wrong password, {tries} attempts left")
#         givenPassword = input("enter your password:   ")
#     elif tries == 0:
#         print("you're out of attempts")
#         break
# else:
#     print("correct password")
#
# my_grades = {
#     "math": "17",
#     "physics": "16",
#     "science": "16",
#     "philosophy": "17"
# }
# for grade in mygrades:
#     print (f"my grade in {grade} is {mygrades.get(grade)}")

# students = {
#     "amine": {
#         "math": "18",
#         "physics": "17",
#         "science": "16"
#     },
#     "khalil": {
#         "math": "14",
#         "physics": "13",
#         "science": "12"
#     },
#     "hicham": {
#         "math": "12",
#         "physics": "13",
#         "science": "11"
#     }
#     }
# for name in students:
#     print(f"{name} grades are:  ")
#     for grades in students[name]:
#         print(f"{grades}:  {students[name][grades]}")

# a = 0
# for x in range(1,10):
#     if x % 2 == 0:
#         print(x)
#         a += 1
# print(f"we have {a} even numbers")

# numbers = [0, 1, 2, 3, 4, 5, 6, 7]
# for num in numbers:
#     print(num)
#     if num == 5:
#         print("you got a five in here")

# MyGrades = {
#     "math": "18",
#     "physics": "17",
#     "science": "16"
# }
# for grade in MyGrades:
#     print(f"{grade} ==> {MyGrades[grade]}")
# print(MyGrades)
# print(MyGrades.items())

# for grade_key, grade_value in MyGrades.items():
#     print(f"{grade_key} ==> {grade_value}")

# students = {
#     "amine": {
#         "math": "18",
#         "physics": "17",
#         "science": "16"
#     },
#     "khalil": {
#         "math": "14",
#         "physics": "13",
#         "science": "12"
#     },
#     "hicham": {
#         "math": "12",
#         "physics": "13",
#         "science": "11"
#     }
#     }
# for student, grades in students.items():
#     print(f"{student} grades are:  ")
#     for module, grade in grades.items():
#         print(f"{module}  ==>  {grade}")

# def say_hi():
#     return "hello by python from inside the function"
# print(say_hi())

# def say_hello(name):
#     print(f"hello {name}")
# say_hello("amine")
# say_hello("sami")
# say_hello("mohamed")

# sum1 = int(input("enter the first number:    "))
# sum2 = int(input("enter the second number:    "))
# def addition():
#     print(sum1+sum2)
# addition()

# def say_hi(*peoples):
#     for name in peoples:
#         print(f"hello {name}")
# say_hi("amine", "mina", "sally", "islam")

# def introduction (name, age, country = "unknown"):
#     print(f"Hello {name} Your Age is {age}, you are from {country}")
# introduction("amine", "20")

# def add(*sum):
#     num = 0
#     for i in sum:
#         num += i
#         result = num
#     return num
# print(add(1, 1, 4, 5 ,6 ))

# skills_with_progress = {
#     "php": "70%",
#     "css": "60%",
#     "ps": "70"
# }
# def hello(name, *args,**kwargs):
#         print(f"hello {name}\nYour Skills Without Progress are :")
#         for skill in args:
#             print(skill)
#         print("your skills with progress are   :")
#         for skill_key, skill_value in skills_with_progress.items():
#             print(f"{skill_key} ==> {skill_value}")
# hello("amine", "python", "JS")

# def function():
#     global x
#     x = 10
#     print(f"local x is {x}")
# print(f"global x before calling the function is {x}")
# function()
# print(f"global x is {x}")

# def clean_Word(word):
#     if len(word) == 1:
#         return word
#     if word[0] == word[1]:
#         return clean_Word(word[1:])
#     return word[0] + clean_Word(word[1:])
# print(clean_Word("eeeeeeeedddddddddiiiiitttttt"))

# introduction = lambda name, age : f"hello {name} your age is {age}"
# print(introduction("amine", 20))



# x = [1, 2, 3, 4, "5"]
# if all(x):
#     print("all elements are true")
# else:
#     print("there is at least one element false")

# x = [[], 5]
# if any(x):
#     print("there is at least one element true")
# else:
#     print("all elements are wrong")

# print(bin(5744))

# a = 1
# b = 2
# print(id(1))
# print(id(2))

# a = [1,45, 5, 5]
# print(sum(a))
# print(round(55.45))
# print(round(22.4574, 2))
# for i in range(9):
#     print(i)
# print(list(range(11)))
# print("hello", "amine", "how", "are", "you",sep=",")
# print(pow(4,5,3))
# full_name = "mohamed amine sedrata"
# first_name = full_name[8:14]
# last_name = (full_name[slice(14,22)])
# print(first_name)
# print(last_name)

'with def'
# def formattxt(text):
#     return (f"- {text} -")
# MyList = ["amine","harry","fury","mohamed"]
# myformattxt = map(formattxt,MyList)
'with lambda'
# for line in map(lambda text : f"- { text} -",MyList):
#     print(line)

# def say_hi(name):
#     return (f"hello {name} its nice seeing you here ")
# friends = ["amine", "hoda", "hicham" ,"samy"]
# welcome = map(say_hi, friends)
# for line in welcome:
#     print(line)

# def checknum(num):
#     if num == 63:
#         return True
# nums = [4,63,6,24,86,12,0]
# checknums = filter(checknum, nums)
# for num in checknums:
#     print(num)
#
# items = [
#     ("product1", 12),
#     ("product2", 15),
#     ("product3", 41)
# ]
# list = []
# for item in items:
#     list.append(item[1])
# print(list)
# prices = list(map(lambda item: item[1],items))
# for item in x:
#     print(item)
# print(prices)

# def add7(x):
#     return x+7
# nums = [1,2,3,4,5,6,7,8,9]
# a = list(filter(add7,nums))
# print(a)

# def isOdd(num1):
#     return num1%2 != 0
# mylist = [1,2,3,4,5,6,7,8,9]
# b = list(filter(isOdd,mylist))
# def add7(num2):
#     return num2 + 7
# c = list(map(add7,b))
# print(c)

# buddies = [("amine", 18),
#            ("hicham", 20),
#            ("khalil", 44),
#            ("ben", 5)]
# age = lambda age : age[1] >= 18
# agechecking = list(filter(age, buddies))
# for line in agechecking:
#     print(line)

# def check(num):
#     if num == 0:
#         return True
# list_of_nums = [0,52,6,7,5,34,12,5]
# x = filter(check, list_of_nums)
# for number in x:
#     print(number)

# def checkName(name):
#     return name.startswith("A")
# friends = ["Amine","osama","Ahmed","ayman"]
# friends_check = filter(checkName,friends)
# for friend in friends_check:
#     print(friend)

# members = ["amine", "harry", "fin", "kane"]
# name = input("type in your name please:  ")
# if name in members:
#     print(f"hello {name} hope you're doing well")
#     status = input("what is it for today")
#     if status == "usual":
#         print("its fine, i'm sure you'll figure something out")
#     else:
#         print("Well, that's new !!!")
# else:
#     print(f"we're sorry {name} you have to be a member in order to take this step")
#     nxt = input(f"would you like to sign up as a member?:      ")
#     if nxt.upper().strip() == "YES":
#         members.append(name)
#         print(members)
#     elif nxt.strip().upper() == "NO":
#         print("sorry to see you leave already, bye")
#     else:
#         print("something went wrong please try again")

# friends =["amine", "cris", "micheal", "fred", "alfred"]
# for friend in filter(lambda name : name.startswith("a"), friends):
#     print(friend)

# from functools import reduce
# def fun(num1, num2):
#     return num1 + num2
# NumList = [36,67,62,66,4,44]
# x = reduce(fun,NumList)
# print(x)

# from functools import reduce
# letters = ["H", "E", "L", "L", "O"]
# for letter in letters:
#     print(letter, end="")
# def sumall(let1 ,let2):
#     return let1 + let2
# result = reduce(sumall,letters)
# print(result)

# factorial = [5,4,3,2,1]
# import functools
# def fac(num1,num2):
#     return num1*num2
# result = functools.reduce(fac,factorial)
# print(result)

# list = [1,2,3,4,5,6,7,8,9,10]
# def bla(num):
#     return num**num
# result = map(bla,list)
# for i in result:
#     print(i)

# MySkills = ["html", "css", "java", "python"]
# MySkillsCounter = enumerate(MySkills, 1)
# for a ,b in MySkillsCounter:
#     print(f"{a} ==> {b}")

# print(help(help))

# list = ["amine", "steve", "son", "martin"]
# list_counter = enumerate(list, 1)
# for num, name in list_counter:
#     print(f"{num + 0} ===> {name}")
# r_list = reversed(list)
# for r in r_list:
#     print(r)

# variable = reversed("nima")
# for i in variable:
#     print(i, end="")
# 
# import pyfiglet
# import termcolor

# temperature = int(input("what's the temperature outside :   "))
# if temperature > 35:
#     print("its hot outside stay Home")
# elif temperature < 20:
#     print("its freezing outside you should stay Home")
# else:
#     print("the weather is fine today i suppose you go outside")


# def add(*nums):
#     sum = 0
#     for index in nums:
#         sum += index
#     return sum
# print(add(78,98,66,9))

# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f = f*i
#     return f
# print(fact(3))

# def addition(name):
#     return f"{name}us"
# names = ["amin", "uran", "among ", "th"]
# result = map(addition, names)
# for i in result:
#     print(i)
# from functools import reduce


# list_of_nums =[35,52,5,2,5,62,6,65]
# def multiplier(x, y):
#     return x*y
# x = reduce(multiplier, list_of_nums)
# print(x)

# list_of_nums =[35,52,5,2,5,62,6,0,"",65]
# x = filter(None, list_of_nums)
# for i in x:
#     print(i,end=",")

# name = "amine"
# if name == "amine":
#     print("its him")
# else:
#     print("we missed him")

# dic = {
#   "amine": 20,
#   "harry": 33,
#   "steve": 37,
#   "scarlet": 30
# }
# print(type(dic))
# for n, t in dic.items():
#   print(f"{n} age is {t}")

# from random import random
# print(random())
# print(0.1 + 0.2 )

# import turtle
# print(dir(turtle))

# print("="* 50)
# from random import  randint
# name = (randint(0,5))
# while name != 5:
#   print(name)
# print(randint(0,100))

# import mymodule as x
# print(x.aaa("you"))

# from mymodule import aaa as a

# import termcolor
# import pyfiglet
# import colorama
# print(dir(pyfiglet))
# print(pyfiglet.figlet_format((termcolor.colored("Amine", color="red"))))
# print(termcolor.colored(pyfiglet.figlet_format("Elzero"), color="yellow"))
# print(termcolor.colored("Elzero", color="yellow"))
# print(pyfiglet.figlet_format("CR7"))
# print(termcolor.colored(pyfiglet.figlet_format("Elzero"),color="yellow"))

# import pyfiglet
# import termcolor
# import colorama
# colorama.init()
# print(termcolor.colored("amine", color="yellow"))

# print("="*100)
# import sys
# print(sys.path)

# import termcolor
# import pyfiglet
# import colorama
# colorama.init(autoreset=True)
# print(termcolor.colored(pyfiglet.figlet_format("amine"),color="yellow"))
# import colorama
# from colorama import Fore, Back, Style
# colorama.init()
# print(f"{Fore.RED}{Back.GREEN}{Style.BRIGHT} i'm red backgrounded green")

# from random import randint
# print(randint(0,10))

# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.min)
# print(datetime.datetime.max)
# print(datetime.datetime.now().time().hour)
# print(datetime.datetime.now().time().minute)
# print(datetime.datetime.now().time().second)
# print(datetime.time.min)
# print(datetime.time.max)
# print(datetime.datetime(2002,4,6))
# print(datetime.datetime(2002,4,6,5,55,33,83976))

# BirthYear = int(input("What year have you been born?:   "))
# BirthMonth = int(input("What month have you been born?:   "))
# BirthDay = int(input("What day have you been born?:   "))
# birthday = (datetime.datetime(BirthYear,BirthMonth,BirthDay))
# DateNow = datetime.datetime.now()
# DaysLived = (f"{(DateNow - birthday).days}")
# print(f"You've been alive for {DaysLived} days")

# import time
# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)


# import datetime
# birthday = datetime.datetime(2002,4,6)
# print(birthday.strftime)

# from functools import reduce
# def sumall(num1, num2):
#     return num1 * num2
# list = [43,52,64,23,5,]
# result = reduce(sumall,list)
# print(result)

# import datetime
# MyBirthday = datetime.datetime(2002,4,6)
# print(MyBirthday)
# print(MyBirthday.strftime("%B"))
# print(MyBirthday.strftime("%a"))   this is the same
# print(f"{MyBirthday:%a}")              as this
# print(MyBirthday.strftime("%A"))
# print(MyBirthday.strftime("%w"))
# print(MyBirthday.strftime("%d"))
# print(MyBirthday.strftime("%-d"))
# print(MyBirthday.strftime("%b"))
# print(MyBirthday.strftime("%m"))
# print(MyBirthday.strftime("%-b"))
# print(MyBirthday.strftime("%I"))

# name = "amine"
# for letter in name:
#     print(letter,end="=")
# num = 10

# string = "amxnese"
# iterator = iter(string)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for letter in "BroCode":
#     print(letter)

# def Generator():
#     yield "someday"
#     yield "i'm gonna appreciate myself"
#     yield "for not giving up"

# myGen = Generator()
# print(next(myGen))
# print(next(myGen))
# print(next(myGen))
# print(next(myGen))

# for index in myGen:
#     print(index)
# ListOfNames = ["osama", "amine", "khaled"]
# itered = iter(ListOfNames)
# print(next(itered))
# print(next(itered))
# print(next(itered))
# print(next(itered))

# def gen():
#     yield "getting wormed up"
#     yield "getting into it"
#     yield "almost there"
#     yield "loading some oponents"
#     yield "finished"
#     yield "its ready to be launched"
# mygen = gen()
# print(next(mygen))
# print("the beggining")
# print(next(mygen))
# print("getting to the point")
# print(next(mygen))
# print("last touches")
# print(next(mygen))
# for lines in mygen:
#     print(lines)

# name = "function"
# for letter in name:
#     print(letter)

# print("=" * 50)
# def CleanWord(word):

#     if len(word) == 1:

#         return word

#     if word[0] == word[1]:
#         print(f"before return ==>  {word}")
#         return CleanWord(word[1:])
#     print(f"after return ==>  {word}")
#     return word[0] + CleanWord(word[1:])

# print(CleanWord("ppppyyyyyytttttthhhhhhooooooooonnnnnnnnnnn"))

# def say_hello(name):
#     return "say hello {name}"

# print("=" * 50)
# def Decorator(fun):
#   def nested(*nums):
#     for num in nums:
#       if num < 0:
#         print("Beware! there is at least one number less than zero")
#     fun(*nums)
#   return nested
# def Decorator1(fun):
#   def nested1(*nums):
#     print("saying hello from  the second decorator")
#     fun(*nums)
#   return nested1
# @Decorator
# @Decorator1
# def add(num1, num2, num3):
#   print(num1 + num2 + num3)
# add(22,4, -55)

# from time import time
# def decorator(fun):
#   def speed_test():
#     start = time() 
#     fun()
#     end = time()
#     print(f"time token to run your function is:  {end - start}")
#   return speed_test
# @decorator
# def bignum():
#   for i in range(1, 20000):
#     print(i)
# bignum()

# list1 = [1,2,3,4,5]
# list2 = ["A","B","C"]
# tuple1 = ("woman", "man","girl", "boy")
# dict1 = {"amine": 20 ,"harry": 32,"terry":5}
# ultimateList = zip(list1,list2,list3)
# for item in ultimateList:
#     print(item)
# for item1, item2,item3,item4 in zip(list1, list2, tuple1, dict1):
#     print("List 1 item ==>", item1)
#     print("List 2 item ==>", item2)
#     print("tuple 1 item ==>", item3)
#     print("dict1 key ==>", item4, ", dict1 value ==>", dict1[item4])



# def aminefunc(name):
#     """
#     this is amine function
#     its purpose is saying hello to the user
#     it has been made by amine himself so he can greet people he can't meet
#     """
#     print(f"hello {name} from amine")
# print(aminefunc.__doc__)
# print(sum.__doc__)





# x = -10
# if x < 0:
#     raise Exception(f"the number {x} is less than zero")
# else:
#     print("you're all good")

# y = "amine"
# if type(y) != int:
#     raise ValueError("only numbers allowed")
# else:
#     print("its all good")

# try:
#     number = int(input("enter a number:   "))
#     print("the given input is an integer from try ")
# except:
#     print("the given input is not an integer ")
# else:
#     print("the given input is an integer from else")
# finally:
#     print("this line  will appear no matter what")


# try:
#     print(int(77))
# except ValueError:
#     print("value error, please check the given input")
# except ZeroDivisionError:
#     print("can never divide by zero")
# except NameError:
#     print("there were some problems identifying")
# except:
#     print("something went wrong, please make sure that the given code is clean")
# else:
#     print("the code that has been writen is clean")
# finally:
#     print("all ways leads to rome")



# try:
#     print(int("amine"))
# except ValueError:
#     print("only numbers are accepted")
# except ZeroDivisionError:
#     print("can't divide by zero")
# except NameError:
#     print("there were some problem with the identifier ")
# except:
#     print("something went wrong")
# else:
#     print("you're all good")
# finally:
#     print("all rodes leads to rome")




# def say_hi(name) -> str:
#     print(f"hello {name}")
# say_hi("amine")
# def sum(n1,n2) -> int:
#     print(n1+n2)
# sum("amine","sdrt")

# [A-z0-9\.]+@[A -z0-9]+\.[A-z]+  ==> email matching
# (\d{3}) (\w{4}) (\(?\w{3}\)?)
# \d(-|\)|>) \w+

# import re

# my_search = re.search(r"\w{3}","amine5")
# print(my_search.span())
# print(my_search.string)
# print(my_search.group())
# print(my_search)
# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@@osama.com")
# if is_email:
#     print("the input given is a valid email")
# else:
#     print("validation denied")

# email_given = input("please enter your email:  ")
# search = re.findall("[A-z0-9\.]+@[A-z0-9]+\.(com|net)",email_given)
# list = []
# if search != []:
#     list.append(email_given)
#     print("email succesfully added to the list")
#     print(list)
# else:
#     print("input given has not been considered as an email")

# x = "i love the programing language named python"
# print(y)
# string = "how-to-write_a_very-good-article"
# for i,d in enumerate(stringed):
#     if len(d) < 2:
#         continue
#     else:
#         print(f"word number : {i+1} ==> {d}")

# import os
# print("="*50)
# print(os.getcwd())
# print("="*50)

# import re
# x = "just wanted it to feel more practical"
# z = re.sub("\s","...",x)
# print(z)

# my_web = ("https://www.elzero.org:8080/category.php?article=105?name=how-to-do")
# my_search = search("(https?)://(www)?\.?(\w+)\.(\w+):(\d+)?/?(.+)",my_web)
# # print(my_search)
# # print(dir(my_search))
# # print(my_search.group())
# # print(my_search.groups())
# for group in my_search.groups():
#     print(group) 


# def yields():
#     yield "first"
#     yield "second"
#     yield "third"
# nxt = yields()
# print(next(nxt))
# print(next(nxt))
# print(next(nxt))

# string = "crazy"
# x = iter(string)
# print(next(x),end="==>")
# print(next(x),end="==>")
# print(next(x),end="==>")
# print(next(x),end="==>")
# print(next(x))

# from functools import reduce
# list = [4,35,3,277,4]
# def sumall(num1,num2):
#     return num1 + num2
# x = reduce(sumall,list)
# print(x)


# import sqlite3
# db = sqlite3.connect("app.db")
# cr = db.cursor()
# db.execute("CREATE TABLE if not exists skills(name text ,progress integer, user_id integer)")
# cr.execute("CREATE TABLE if not exists users (user_id integer , name text)")
# cr.execute("insert into users (user_id,name) values(6871,'amine')")
# cr.execute("insert into users (user_id,name) values(5746,'hicham')")
# cr.execute("insert into users (user_id,name) values(7564,'youcef')")
# db.commit()
# db.close()

# mylist = ["amine", "hisham","samy", "steve","najwa","mohamed"]
# import sqlite3
# db = sqlite3.connect("new")
# cr = db.cursor()
# cr.execute("create table if not exists members (name_id integer,name text)")
# for key, value in enumerate(mylist):
#     cr.execute(f"insert into members (name_id,name) values({key+1},'{value}')")
# cr.execute("select * from members")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchall())
# print(cr.fetchmany(3))
# db.commit()
# db.close()
# print(sqlite3.__doc__)

# import sqlite3
# try:
#     db = sqlite3.connect("new.db")
#     print("connected to the database successfully")
#     cr = db.cursor()
#     cr.execute("create table if not exists members(name text,name_id integer)")
#     ### cr.execute("insert into members(name,name_id) values ('steve',4)")
#     db.commit()
#     cr.execute("select * from members")
#     result = cr.fetchall()
#     print(result)
#     print(f"you have {len(result)} rows in your table")
#     for rows in result:
#         print("showing data")
#         print(f"username is ==> {rows[0]},and user's id is ==> {rows[1]}")
#     db.close()
# except sqlite3.Error as er:
#     print(f"error reading data {er}")
# finally:
#     if db():
#         db.close()
#         print("database closed")

# import sqlite3
# db = sqlite3.connect("new.db")
# cr = db.cursor()
# # cr.execute("update members set name = 'clause' where name_id = 1")
# cr.execute("delete from members where name_id = 4")
# cr.execute("select * from members")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# db.commit()


# members = ["amine","samuel","mohamed","adam"]
# name = input("please insert your name:  ")
# if name in members:
#     db = sqlite3.connect("new.db")
#     cr = db.cursor()
#     cr.execute("select * from members")
#     print(f"hello {name} welcome to the database of yours")
#     status = input("how do you want to mess with your database:   ").upper().strip()
#     if status == "UPDATE":
#         print("showing data")
#         result = cr.fetchall()
#         for i in result:
#             print(f"username is ==> {i[0]}, and name_id is ==> {i[1]}")
#         id = input("please enter the id of the name that you want to update  :  ==>  ")
#         new_name = input("please enter the new name   ==>  ")
#         cr.execute(f"update members set name = '{new_name}' where name_id = {id}")
#         db.commit()
#         print("showing updated data")
#         for i in result:
#             print(f"username is ==> {i[0]}, and name_id is ==> {i[1]}")
#         db.close()
#         print("database closed")
# else:
#     print("name not found")

# import sqlite3
# members = ["amine","samuel","mohamed","adam"]
# name = input("please insert your name:  ")
# if name in members:
#     db = sqlite3.connect("app.db")
#     cr = db.cursor()
#     cr.execute("select * from user")
#     print(f"hello {name} welcome to the database of yours")
#     print(cr.fetchall())
# else:
#     raise NameError("the name you added has not been found")
# command_list = ["a","u","d","s","q"]
# input_var ='''
# what command do you want to apply
# "a" ==> add user
# "u" ==> update user
# "d" ==> delete user
# "s" ==> show users
# "q" ==> quit database
# Choose an option:
# '''
# def cac():
#     db.commit()
#     cr.close()
# user_input = input(f"{input_var} ==>  ")
# def add_user():
#     name = input(f"enter the new user's name:   ").lower().strip()
#     sk = input("enter the new user's skill:   ").lower().strip()
#     nid = input("enter the new user's id:   ")
#     cr.execute(f"select name_id from user  where name_id = '{nid}'")
#     rslt = cr.fetchone()
#     if rslt == None:
#         cr.execute(f"insert into user(name,skill,name_id) values ('{name}','{sk}',{nid})")
#         print("user added succesfully")
#     else:
#         cr.execute(f"select name from user where name_id = {nid}")
#         aun = cr.fetchone()
#         stts = input(f'''
#         the given id has been already used for {aun}
#         would you like to override username?
#         y ===> Yes
#         n ===> No
#         ''').lower()
#         if stts == "n":
#             print("database closed")
#             cac()
#         elif stts == "y":
#             cr.execute(f"update user set name = '{name}' where name_id = {nid}")
#             cr.execute(f"update user set skill = '{sk}' where name_id = {nid}")
#             print("username and skill updated successfully")
#             cac()
# def update_user():
#     status = input('''
#     what are you updating:   
#     n ==>  name
#     s ==>  skill
#     i ==>  name's id
#     choose an option:   
#     ''')
#     if status == "n":
#         id = input("enter the id of the name you want to update:   ")
#         nm = input("inser updated name:   ").lower().strip()
#         cr.execute(f"update user set name = '{nm}' where name_id = {id}")
#         print("name updated successfully")
#         cac()
#     elif status == "s":
#         id = input("enter the id of the skill you want to update:   ")
#         ns = input("insert updated skill:   ").lower().strip()
#         cr.execute(f"update user set skill = '{ns}' where name_id = {id}")
#         print("skill updated successfully")
#         cac()
#     elif status == "i":
#         name = input("enter the username that you want to change his id    :").lower().strip()
#         skill = input("enter the skill of the username that you want to change his id:   ").lower().strip()
#         new_id = input("insert updated id:   ")
#         cr.execute(f"update user set name_id = {new_id} where name = '{name}' and skill = '{skill}'")
#         print("name_id updated successfully")
#         cac()
#     else:
#         raise NameError("the input given is invalid")
# def delete_user():
#     dname = input(f"enter the name you want to delete:   ")
#     nid = input("enter the user's id:   ")
#     cr.execute(f"delete from user where name = '{dname}' and name_id = {nid}")
#     print("user deleted succesfully")
# def show_user():
#     cr.execute("select * from user")
#     users = (cr.fetchall())
#     print(f"there are {len(users)} users stored in the database")
#     for i in users:
#         print(f"username is ({i[0]}), user skill is ==> ({i[1]}), and user id is ({i[2]})")
# if user_input in command_list:
#     if user_input == "a":
#         add_user()
#         cac()
#     elif user_input == "u":
#         update_user()
#         cac()
#     elif user_input == "d":
#         delete_user()
#         cac()
#     elif user_input == "s":
#         show_user()
#         cac()
#     else:
#         print("closed database")
#         cac()
# else:
#     print(f"command '{user_input}' not found")

# import timeit
# import random
# print(timeit.timeit("random.randint(0,50)",setup="import random"))
# print(timeit.repeat("random.randint(0,50)",setup="import random",repeat=4))
# print(timeit.timeit(stmt="'Elzero' * 1000"))

# import logging
# logging.basicConfig(filename="my_app.log",
#                     filemode="a",
#                     format="%(asctime)s %(name)s %(levelname)s %(message)s",
#                     datefmt="%d / %b / %Y %H:%M:%S")
# my_logger = logging.getLogger("amine")
# my_logger.warning("this is warning message") 

# import string
# import random
# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)

# def Serial(count) -> int:
#     all_chars = string.ascii_letters + string.digits
#     chars_num = len(all_chars)
#     serial_list = []
#     while count > 0:
#         random_num = random.randint(0,chars_num - 1)
#         random_char = all_chars[random_num]
#         serial_list.append(random_char)
#         count -= 1
#     print("".join(serial_list))
# Serial(20)

# import string
# def find_missing_letter_in(giv_lett):
#     letters = string.ascii_lowercase
#     x = 0
#     z = giv_lett[0]
#     while letters[x] != z:
#         x += 1
#     xxx = 0
#     while letters[x] == giv_lett[xxx]:
#         xxx += 1
#         x += 1
#     else:
#         print(f"the letter ({letters[x]}) is the missing letter")
# find_missing_letter_in("abcdefgijk")
# find_missing_letter_in("cdefghijklmnoqrs")

# def fmli(gl):
#     letters = string.ascii_lowercase
#     start = letters.index(gl[0])
#     for letter in letters[start:]:
#         if letter not in gl:
#             return letter
# print(fmli("abcdefhijk"))

# def reverse1(given_int):
#     x = str(given_int)
#     r = reversed(x)
#     for i in r:
#         print(i,end="")
# reverse1(123456789)
# def reverse2(given_int):
#     x = str(given_int)
#     r = x[::-1]
#     for i in r:
#         print(i,end="")
# reverse2(123456789)

# def longest_word(sentence):
#     max = 0
#     for i in splited:
#         if len(i) > max:
#             max = len(i)
#             longest = i
#     return longest
# print(longest_word("i love pizza"))

# def remove(word,letter):
#     clean = []
#     for i in word:
#         if i == letter:
#             continue
#         clean.append(i)
#     print("".join(clean))
# remove("it's ok@ay if@ you@ find it hard@ at first" , "@")

# def remove(word):
#     result = filter(lambda x:x != "@" and x != "#" and x != "3" ,word)
#     return "".join(result)
# print(remove("3it3#33's ok@a33#y #if3@ 3y##ou@ 33#fi#n3#d #it# 33##ha3r3d@ at 333#f#ir3s3t33#33333"))

# def re_duplicated(sentence):
#     x = sentence.split(" ")
#     result = []
#     for i in x:
#         if i not in result:
#             result.append(i)
#     return " ".join(result)
# print(re_duplicated("i love web web development"))

# def re_duplicated(sentence):
#     x = sentence.split(" ")
#     result = list(dict.fromkeys(x))
#     return " ".join(result)
# print(re_duplicated("i love web web development"))

# def add_us_and_commas(number):
#     string = str(number)
#     list_of_nums = []
#     count = 0
#     for i in string:
#         list_of_nums.append(i)
#         count +=1
#         if count / 3 == 1:
#             list_of_nums.append("_")
#         elif count / 3 > 1 and count % 3 == 0:
#             list_of_nums.append(",")
#     return "".join(list_of_nums)
# print(add_us_and_commas(797296598687587174))
# def add_us_and_commas(number):
#     formatted = f"{number:,}"
#     if len(formatted) > 3:
#         spl = formatted.split(",")
#         all_but_last = spl[:-1]
#         fjoin = "".join(all_but_last)
#         ijoin = int(fjoin)
#         return f"{ijoin:,}_{spl[-1]}"
#     return formatted
# print(add_us_and_commas(797296598687587174))

# def series_resistance(nums):
#     return "{} ohm{}".format(sum(nums),"s" if sum(nums)>=2 else "")
# print(series_resistance([8,8]))

# def ds(nums):
#     print("{} ohm{}".format(sum(nums),"s" if sum(nums)>=2 else ""))
# ds([42,24,41])

# def series_resistance(lst):
# 	total = sum(lst)
# 	return '{} ohm{}'.format(total, 's' * (total > 1))
# print(series_resistance([2,24,41,1]))

# formatting
# for i in range(1,11):
#     print(f"{i:02}")
# from math import pi
# num = pi
# print(f"{num:.4f}")
# def series_resistance(lst):
# 	total = sum(lst)
# 	return '{} ohm{}'.format(total, 's' * (total > 1))

# def is_curzon(num):
#     x = 2 ** num + 1
#     y = 2 * num + 1
#     if x % y == 0:
#         return True
#     else:
#         return False

# def stutter(word):
#     if len(word) >= 2:
#         two = word[:2]
#         return "{}... {}... {}?".format(two,two,word)
# print(stutter("incredible"))

# def calculator(num1, operator, num2):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         if num2 == 0:
#             return "Can't divide by 0!"
#         return num1 / num2
# print(calculator(5,"/",0))

# def calculator(n1, operator, n2):
# 	try: 
# 		return eval(str(n1)+operator+str(n2))
# 	except ZeroDivisionError:
# 		return "Can't divide by 0!"
# print(calculator(2,"*",5))

# def factorial(num):
#     if num >= 0:
#         neg_one = num - 1
#         while neg_one > 1:
#             num *= neg_one
#             neg_one -= 1
#         return num
# print(factorial(0))

# import math
# def end_corona(recovers, new_cases, active_cases):
#     if recovers > new_cases:
#         average = recovers - new_cases
#         days_left = active_cases/average
#         return math.ceil(days_left)

# def dis(price, discount):
#     x = (discount/100)*price
#     result = price - x
#     return round(result,2)

# def weight(r, h):
#     import math
#     result = (math.pi*r*r*h)*0.001
#     return round(result,2)

# def is_triplet(n1, n2, n3):
#     x = max(n1,n2,n3)**2
#     z = (n1**2+n2**2+n3**2)-x
#     if x == z:
#         return True
#     else:
#         return False

# def damage(damage, speed, time):
#     if damage < 0 or speed < 0:
#         return "invalid"
#     x = damage*speed
#     if time == "second":
#         return x
#     elif time == "minute":
#         return x*60
#     elif time == "hour":
#         return x*3600

# def damage(damage, speed, time):
# 	secs = {'second':1, 'minute':60, 'hour':3600}
# 	ans = damage*speed*secs[time]
# 	return ans if ans>0 and speed>0 else 'invalid'

# from math import pi
# def radians_to_degrees(rad):
#     x = rad*(180/pi)
#     return round(x,1)
# print(radians_to_degrees(1))

# def counterpartCharCode(char):
#     if char.isupper():
#         return ord(char.lower())
#     else:
#         return ord(char.upper())

# def counterpartCharCode(char):
# 	return ord(char.swapcase())
# print(counterpartCharCode("a"))

# def to_camel_case(text):
#     for i in text:
#         if i == "-"
#             index = index(text,"-")

# to_camel_case("jlkf")
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# def spin_words(sentence):
#     result = []
#     for word in sentence.split():
#         if len(word) >= 5:
#             result.append(word[::-1])
#         else:
#             result.append(word)
#     return " ".join(result)

# def filter_list(l):
#     result = []
#     for i in l:
#         if type(i) == int:
#             result.append(i)
#     return result
# def unique_in_order(iterable):
#     newList = []
#     for item in iterable:
#         if len(newList) < 1 or not item == newList[len(newList) - 1]:
#             newList.append(item)
#     return newList
# print(unique_in_order('AAAABBBCCDAABBB'))

# def is_square(n):
#     if n < 0 or str(n**0.5).split(".")[1] != "0":
#         return False
#     else:
#         return True

# import math
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;
# print(is_square(3))

# def unique_in_order(iterable):
#     newlist = []
#     for i in iterable:
#         if len(newlist) == 0 or i != newlist[len(newlist)-1]:
#             newlist.append(i)
#     return newlist
# print(unique_in_order('AAAABBBCCDAABBB'))

# def dig_pow(n, p):
#     newlist = []
#     for i in str(n):
#         newlist.append(int(i)**p)
#         p += 1
#         final = str((sum(newlist))/n).split(".")
#     if final[1] == "0":
#         return final[0]
#     else:
#         return -1

# def dig_pow(n, p):
#     s = 0
#     for i,c in enumerate(str(n)):
#         s += pow(int(c),p+i)
#     return s/n if s%n==0 else -1

# def cakes(recipe, available):
#     list_of_num = []
#     list_of_str = []
#     result = []
#     x = 0
#     for i,n in recipe.items():
#         list_of_num.append(n)
#         list_of_str.append(i)
#     z = len(list_of_num)
#     for a,b in available.items():
#         list_of_num.append(b)
#         list_of_str.append(a)
#     if z > len(list_of_num)-z:
#         return 0
#     while len(list_of_num)-1 > z:
#         result.append(list_of_num[z]/list_of_num[x])
#         x += 1
#         z += 1



# import string
# x = string.ascii_letters + string.digits + string.punctuation + " "
# print(x)
# def duplicate_encode(word):
#     first_list = []
#     final_result = []
#     z = word.lower()
#     for i in z:
#         first_list.append(i)
#     for n in x:
#         if n in first_list:
#             first_list.remove(n)
#     for a in z:
#         if a in first_list:
#             final_result.append(")")
#         else:
#             final_result.append("(")
#     return "".join(final_result)

# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# from collections import Counter
# def duplicate_encode(word):
#     return "".join(("(" if Counter(word)[i] == 1 else ")") for i in word.lower())
# print(duplicate_encode("amiine"))

# from collections import Counter
# ll = []
# word = "abbcccddddeeeeeffffffggggggghhhhhhhiiiiiiiijjjjjjjjjkkkkkkkkkk"
# for i in word:
#     ll.append((Counter(word)[i]))
# for n in ((dict.fromkeys(ll))):
#     print(n,end=",")



# 

# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.min)
# print(datetime.datetime.max)
# print(datetime.datetime.now().time().hour)
# print(datetime.datetime.now().time().minute)
# print(datetime.datetime.now().time().second)
# print(datetime.time.min)
# print(datetime.time.max)
# print(datetime.datetime(2002,4,6))
# print(datetime.datetime(2002,4,6,5,55,33,83976))

# import datetime
# def make_readable(seconds):
#     if seconds < 60:
#         return str(datetime.time(0,0,seconds))
#     elif seconds < 3600:
#         min1 = (int(seconds/60))
#         return str(datetime.time(0,min1,seconds%60))
#     elif seconds <= 86399:
#         hours = (int(seconds/3600))
#         min = int((seconds%3600)/60)
#         sec = int(((seconds%3600)%60))
#         return str(datetime.time(hours,min,sec))
#     elif seconds <= 359999:
#         hours1 = (int(seconds/3600))
#         min2 = int((seconds%3600)/60)
#         sec1 = int(((seconds%3600)%60))
#         if min2<10:
#             min2=f'0{min2}' 
#         if sec1<10:
#             sec1=f'0{sec1}'
#         return f"{hours1}:{min2}:{sec1}"

# def make_readable(s):  
#     return f'{s // 3600:02}:{s // 60 % 60:02}:{s % 60:02}'

# test.assert_equals(make_readable(0), "00:00:00")
# test.assert_equals(make_readable(5), "00:00:05")
# test.assert_equals(make_readable(60), "00:01:00")
# test.assert_equals(make_readable(86399), "23:59:59")
# test.assert_equals(make_readable(359999), "99:59:59")

# import datetime
# a = datetime.date(2000,1,1)
# b = datetime.timedelta(100)
# print(a+b)

# def soc(y,x=1):
#     return x + y
# print(soc(8,3))

# x = [1,2,3,4,5,6,7,8,9]
# z = (1,2,3,4,5,6,7,8,9)"
# from sys import getsizeof
# print(getsizeof(x))
# print(getsizeof(z))

# import timeit
# list_test = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
# tuple_test = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)
# print(list_test,tuple_test)

# def first_non_repeating_letter(string):
#     for letter in string:
#         x = letter.lower()
#         z = string.lower()
#         if z.count(x) == 1:
#             return letter
#     return ''
''' COOL TRICKS '''
# d1 = {'name':'amine','age':20}
# d2 = {'name':'alex','city':'Biskra'}
# merged_dic = {**d1,**d2}
# merged_dic = d1 | d2
# print(d1)
# print(d2)
# print(merged_dic)

# name = 'amin'
# a,b,c,d, = name
# print(a,b,c,d)

# fname = 'sedrata'
# lname = 'amine'
# fname, lname = lname, fname
# print(fname,lname)

# for _ in range(0,25):
#     print(0,end=',')

# def sum(n1,n2,n3,n4):
#     return n1+n2+n3+n4
# ns = [1,2,4,6]
# print(sum(*ns)

# lst = [[4,2],[2,6],[1,5],[3,9]]
# lst.sort(key=lambda x:x[1])
# print(lst)

# import itertools
# lst = [3,5,24,5,2]
# x = itertools.accumulate(lst)
# for i in x:
#     print(i,end=' ')

# lst1 = [1,2,3,4,5]
# lst2 = ['A','B','C','D','E']
# chain_lst = itertools.chain(lst1,lst2)
# for i in chain_lst:
#     print(i,end='')

# def solution(number):
#     return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])
# factorial = [6,5,4,3,2,1]
# from functools import reduce
# def fac(num1,num2):
#     return num1*num2
# result = reduce(fac,factorial)
# print(result)

# def zeros(n):
#     x = n/5
#     return x+zeros(x) if x else 0
# print(zeros(646464))

# for i in range(0,11):
#     if i%2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# from sys import exit
# list = [3,3,4,2,2,5,6]
# if 3 in list
#     print("found")
#     exit(0)
# print("not found")
# exit(1)

# from time import time
# from string import digits
# from itertools import product
# start = time() 
# for x in product(digits,repeat=4):
#     print(*x)
# end = time()
# print(f"time token to run your function is:  {end - start}")

# starting up with a  quiz game

# name = input("what is your name:   ")
# age = input("how old are you:   ")
# print(f"hello {name} you are {age} yo")


# from random import randint
# random_num = randint(0,100)
# answer = 109
# while answer != random_num:
#     answer = (input("guess a number from 0 to 100:   "))
#     if answer.isdigit():
#         answer = int(answer)
#     else:
#         raise ValueError("the input given must be an integer")
#     if answer > random_num:
#         print("Lower")
#     elif answer < random_num:
#         print("Higher")
# print(f"{answer} is the number")

# t = 92579702
# for i in range(2000000000):
#     if i == t:
#         print(i)
#         quit()


# import datetime
# a = int(input("insert the year you were born in:  "))
# b = int(input("insert the month you were born in:  "))
# c = int(input("insert the day you were born in:   "))
# d = int(input("insert the year you're in:  "))
# e = int(input("insert the month you're in:  "))
# f = int(input("insert the day you're in:   "))
# birthday = datetime.date(a,b,c)
# today = datetime.date(d,e,f)
# age = (today - birthday).days
# if age/30/12 > 18:
#     print("you're an adult")
# else:
#     print("you're a mineur")

# lst = []
# lst1 = [23,523,25,5,6]
# lst2 = [42,2,62,1,4]
# index1 = 0
# index2 = 0
# while len(lst1) > index1 and len(lst2) > index2:
#     if lst1[index1] > lst2[index2]:
#         lst.append(lst2[index2])
#         index2 += 1
#     else:
#         lst.append(lst1[index1])
#         index1 += 1
# print(lst)

# lst1 = [1,3,6,98]
# lst2 = [4,5,8,94]
# lst = []
# def merge(listOne ,listTwo):
#     if not listOne or not listTwo:
#         return;
#     else:
        
# a = input("enter a number:   ")
# b = input("enter a number:   ")
# c = input("enter a number:   ")
# if a>b and b>c:
#     print(a,b,c)
# elif a>b and c>b:
#     print(a,c,b)
# elif b>a and a>c:
#     print(b,a,c)
# elif b>c and c>a:
#     print(b,c,a)
# elif c>b and b>a:
#     print(c,b,a)
# else:
#     print(c,a,b)

# def reverse(string):
#     a = []
#     if string == "":
#         return a
#     a.append(string[len(string)-1])
#     reverse(string[:-1])
# print(reverse("hellothere"))

'''       RECURSION       '''

# def fact(x):
#     if x == 0:
#         return 1
#     else:
#         return(x*fact(x-1))
# print(fact())

# def fib(x):
#     if x > 2:
#         return fib(x-1) + fib(x-2)
#     else:
#         return 1
# print(fib(3))

# def frog(feet):
#     ways = 1
#     minus = 1
#     multi = 0
#     if feet == 1:
#         minus += 1
#         ways += (multi-minus)*minus
#         if minus == feet:
#             return ways
#         else:
#             return(frog(feet-minus))
#     multi += 1
#     return(frog(feet-minus))
# print(frog(4))


# ways = 1
# minus = 1
# def frog(feet):
#     global ways
#     global minus
#     if feet == 0:
#         return ways
#         exit()
#     else:
#         ways += minus
#         minus += 1
#         return frog(feet-1)
# print(frog(5))

# ways = 1
# def frog(feet):
#     global ways
#     minus = 1
#     if minus == feet:
#         return ways
#         exit()
#     else:
#         ways = ways + (feet-minus)*minus

#         return frog(feet-minus)
# print(frog(4))

# def frog(feet):
#     if feet == 1:
#         return 1
#     else:
#         return 1 + frog(feet-1) 
# print(frog(96 ))

# def ways(steps):
#     if steps == 0 or steps == 1:
#         return 1
#     else:
#         return ways(steps-2) + ways(steps-1)
# print(ways(4))



# n = int(input("enter the number of steps:   "))
# nums = []
# nums[0] = 1
# nums[1] = 1
# for i in range(2,n):
#     nums.append(nums[i-1] + nums[i-2])
# print(nums)

# def sum_all(n):
#     if n == 0:
#         return 1
#     else:
#         return sum_all(n-1) + sum_all(n-2)
# print(sum_all(5))

# def Reverse( s ):
#     result = ""
#     n = 0
#     start = 0
#     while ( s[n:] != "" ):
#         while ( s[n:] != "" and s[n] != ' ' ):
#             n += 1
#             result = s[ start: n ] + " " + result
#             start = n
#     return result

# def rreverse(s):
#     if s == "":
#         return s
#     else:
#         return rreverse(s[1:]) + s[0]
# print(rreverse("hello"))

# def rrr(s):
#     if s == "" or len(s) == 1:
#       return s
#     else:
#       return rrr(s[1:]) + s[0]
# print(rrr("amine"))

# def is_palindrome(string):
#     if len(string) == 0 or len(string) == 1:
#       return True
#     elif string[0] == string[-1]:
#       return is_palindrome(string[1:len(string)-1])
#     return False

# def find_binary(num,string):
#     if num == 0:
#       return string
#     string = str(num%2) + string
#     return find_binary(num//2,string)
# for i in range(20):
#     print(find_binary(i,''))

# def count_down(num):
#     if num <= 0:
#       return
#     else:
#       print(num)
#       return count_down(num-1)
# (count_down(10))

# def sum_of_nums(num):
#     if num == 1:
#       return 1
#     else:
#       return num + sum_of_nums(num-1)
# print(sum_of_nums(4))

# def binary_search(num,lst_of_nums):
#     mid = len(lst_of_nums)//2
#     if lst_of_nums[mid] == num:
#       return mid
#     elif lst_of_nums[mid] > num:
#       return mid-2 + binary_search(num,lst_of_nums[:mid])
#     else:
#       return  binary_search(num,lst_of_nums[mid:])
# nums = [-4,-3,-2,-1,1,3,4,6,7,8,9,12,32,122,299]
# print(binary_search(32,nums))

# from functools import lru_cache
# @lru_cache()
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
# for i in range(1,110):
#     print(i,':',fibonacci(i))

# def fib(n):
# 		if n == 1 or n == 2:
# 			return 1
# 		return fib(n-1) + fib(n-2)
# print(fib(6))

# fib_cache = {}
# def fib(n):
# 	if n in fib_cache:
# 		return fib_cache[n]
# 	elif n == 1 or n == 2:
# 		value = 1
# 		return value
# 	elif n > 2:
# 		value = fib(n-1) + fib(n-2)
# 		fib_cache[n] = value
# 		return value
# for i in range(1,101):
# 		print(fib(i)) 

# def merge_sort(lst):
# 	sorted_lst = []
# 	if len(lst) == 1:
# 		return lst
# 	elif len(lst) == 2:
# 		sorted_lst.append(min(lst)),sorted_lst.append(max(lst))
# 		return sorted_lst
# 	else:
# 		return merge_sort(lst[:len(lst)//2]) , merge_sort(lst[len(lst)//2:])
# print(merge_sort([12,3,1,2,4,5,7,6,9]))




# def merge_sort(arr):
# 	if len(arr) > 1:
# 		left_arr = arr[:len(arr)//2]
# 		right_arr = arr[len(arr)//2:]
# 		merge_sort(left_arr)
# 		merge_sort(right_arr)
# 		i,j,k = 0,0,0
# 		while len(left_arr) > i and len(right_arr) > j:
# 			if left_arr[i] > right_arr[j]:
# 				arr[k] = right_arr[j]
# 				j += 1
# 				k += 1
# 			else:
# 				arr[k] = left_arr[i]
# 				i += 1
# 				k += 1
# 		else:
# 			while i != len(left_arr):
# 				arr[k] = left_arr[i]
# 				k += 1
# 				i += 1
# 			while j != len(right_arr):
# 				arr[k] = right_arr[j]
# 				j += 1
# 				k += 1
# arr_test = [2,24,12,4,23,1,232,423,5,34,54,75,86,78,76,5,434]
# merge_sort(arr_test)
# print(arr_test)

'''    LIST COMPREHENSION    '''

# def anagrams(word, words):
#     for i in words:
#         if sorted(i) == sorted(word):
#             print(i)

# def anagrams(word, words):
#     return [i for i in words if sorted(i) == sorted(word)]

# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))#, ['carer', 'racer'])
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))# => ['aabb', 'bbaa']
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])# => ['aabb', 'bbaa']

# def filter_list(l):
#     'return a new list with the strings filtered out'
#     return [i for i in l if type(i) is int]
# print(filter_list([1, 2, "a", "b"]))

# def flatten_the_curve(lst):
#     if len(lst) == 0:
#         return []
#     return [round((sum(lst)/len(lst)),1)]*len(lst)

# lst = [1,3,4,5,6]

# lst1 = []
# for i in lst:
#     if i%2 == 0:
#         lst1.append(i*i)
# print(lst1)

# lst2 = [i*i for i in lst if i%2 == 0]
# print(lst2)

# lst3 = list(map(lambda x:x*x,list(filter(lambda x:x%2==0,lst))))
# print(lst3)

# lst = [(i,n) for i in "abcd" for n in range(4)]
# print(lst)

# lst = []
# for i in "abcd":
#     for n in range(4):
#         lst.append((i,n))
# print(lst)

# names = ['bruce','clark','logan','peter']
# superhero = ['Batman','Superman','Wolverine','Spiderman']
# print(list(zip(names,superhero)))

# my_dict = {}
# for name,hero in zip(names,superhero):
#     my_dict[name] = hero
# print(my_dict)
# my_dict1 = {name:hero for name,hero in zip(names,superhero)if name != "peter"}
# print(my_dict1)





'''    OBJECT ORIENTED PROGRAMMING    '''

# class member():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_name(self):
#         print(f"the name is {}")

# color1 = input("enter a color:  ")
# color2 = input("enter a second color:  ")
# celebrity = input("enter a celebrity name:  ")
# print(f"roses are {color1}\nviolets are {color2}\ni love {celebrity}")

# class Solution(object):
#     def longestValidParentheses(self, s):
#         l1 = []
#         l2 = []
#         for i in s:
#             if i == "(":
#                 l1.append(i)
#             if s[0] == ")":
#                 continue
#         for n in s:
#             if n == ")":
#                 l2.append(n)
#             if s[-1] == "(":
#                 continue
#         return (min(len(l1),len(l2)))*2
# print(Solution.longestValidParentheses(2,")()())"))

# x = 5 if False else 8
# print(x)
# def re(num):
#     return int(num/2)
# print(re(50))

# class Student():
#     def __init__(self,name,age,year,gpa):
#         self.name = name
#         self.age = age
#         self.year = year
#         self.gpa = gpa
#     def student_info(self):
#         print(f"his name is {self.name} ,he's {self.age} years old,he's in {self.year} year, has a gpa of {self.gpa} ")
# std1 = Student("amine",20,"First",4.1)
# std1.student_info()


# class member():
    # def __init__(self):
        # print("a new member has been added")
# member()
# member()
# member()
# print(dir(member))
# member_one = member()
# member_two = member()
# member_three = member()
# print(member_one.__class__)

# import pyfiglet
# import termcolor
# import colorama
# colorama.init()
# print(pyfiglet.figlet_format("amine"))
# print(termcolor.colored(pyfiglet.figlet_format("amine"), "red"))

# class object():
#     def __init__(self):
#         print("hello there i love python")
# object()

# def dec(name):
#     return (f"==({name})==")
# list = ["samy", "danzo", "steve", "coman"]
# x = map(dec,list)
# for line in x:
#     print(line)

# class Member():
#     def __init__(self):
#         self.name = "amine"
#         self.age = 20
#         self.job = "web development"
# member_one = Member()
# member_two = Member()
# member_three = Member()
# print(member_one,member_two,member_three)

# friends = ["amine","samy","kiloa","housam"]
# def dec(name):
#     if name == "amine" or name == "kiloa":
#         return (f"{name} is awesome")
#     else:
#         return (f"{name} is the name")
# precise = map(dec,friends)
# for line in precise:
#     print(line)

# class Car():
#     def __init__(self):
#         self.model = "mustang"
#         self.year = 2022
#         self.color = "red"
# car1 = Car()
# print(car1.__class__)

# class user():
#     @staticmethod
#     def say_hello():
#         return f"welcome to this fucked up class"
#     not_allowed_names = ["hell", "shit", "punk"]
#     users_num = 0 
#     @classmethod
#     def show_users_num(cls):
#         return f"we have {cls.users_num} users in our system"
#     def getName(self):
#         return f"{self.name}"
#     def setName(self, newName):
#         self.name = newName
#     def __init__(self, first_name,age, job, sex):
#         self.name = first_name
#         self.age = age
#         self.job = job
#         self.sex = sex
#         user.users_num += 1
    # def fullInfo(self):
#         if self.name in user.not_allowed_names:
#             raise ValueError("name not allowed")
#         else:
#             return f"{self.name}, {self.age}yo, {self.job}"
#     def say_hi(self):
#         if self.sex == "male":
#             return f"hello mr {self.name}"
#         else:
#             return f"hello mrs {self.name}"
# first_name,age, job, sex
# user1 = user("amine",20,"male")
# user1.show_users_num()
# print(user.say_hello())
# print(user.users_num)
# user1 = user("steve",50,"doctor", "male")
# user2 = user("samy",40,"teacher", "male")
# user3 = user("carl",30,"programmer", "male")
# user4 = user("sarah",22,"model", "female")
# print(user.users_num)
# print(user.show_users_num())
# print(f"{user1.name} is {user1.age} he is a {user1.job}")
# print(f"{user2.name} is {user2.age} he is a {user2.job}")
# print(f"{user3.name} is {user3.age} he is a {user3.job}")

# my_string = "amine"
# print(type(type))
# print(type(my_string))
# print(my_string.__class__)
# # print(dir(my_string))
# print(my_string.upper())
# print(str.upper(my_string))

# class skill():
#     def __init__(self):
#         self.skills = ["html", "python", "css"]
#     def __str__(self):
#         return f"my skills are ==> {self.skills}"
# profile = skill()
# print(profile)

# mems = ["amine", 20, True]
# print(f"his name is {mems[0]} he's {mems[1]}, he consider himself as a {mems[2]}")
# for index in mems:
#     print(index)

# name = "amine"
# print("hello {}".format(name))

# class user():
#     def __init__(self, first_name,last_name,age, job):
#         self.__first = first_name
#         self.__last = last_name
#         self.__age = age
#         self.__job = job
#     @property
#     def fullname(self):
#         return f"{self.__first} {self.__last}"
#     @fullname.setter
#     def fullname(self, new):
#         self.__first,self.__last = new.split(" ")
# user1 = user("steve","harvey",50,"doctor")
# user2 = user("samy","zain",40,"teacher")
# user3 = user("carl","jun",30,"programmer")
# user1.fullname = "steve jobs"
# print(user1.fullname)
# print(user1._user__name)
# print(user1.getName())
# user1.setName("taliska")
# print(user1.getName())
# print(user1.describe())
# class person():
#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def describe(self):
#         return f"his name is {self.name} he's {self.age} he is {self.height}mm tall"
# class man(person):
#     def __init__(self, name, age, height, gender):
#         super().__init__(name,age,height)
#         self.gender = gender
# man1 = man("steve",22,178,"male")
# print(man.describe(man1))
# print(person.describe(man1))
# print(man1.describe())

# class Man():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __add__(self,other):
#         names = f"names combined are {self.name} and {other.name}"
#         ages = f"ages combined are {self.age + other.age}"
#         return f"{names} and {ages}"
# man1 = Man("dre",22)
# man2 = Man("trevor",23)
# print(man1+man2)

# my_string = "sting"
# print(my_string.__class__)
# print(my_string.upper())
# print(str.upper(my_string))

# class Skill:
#     def __init__(self):
#         self.skills = ["css", "java", "python"]
#     def __str__(self):
#         return f"my skills are {self.skills}"
#     def __len__(self):
#         return len(self.skills)
# profile = Skill()
# print(profile)
# print(len(profile))

# class Food():
#     def __init__(self,name):
#         self.name = name
#         print(f"{self.name} is created from base method")
#     def eat(self):
#         print("eat method from base class")
# class Apple(Food):
#     def __init__(self,name):
#         super().__init__(name)
# # food1 = Food("pizza")
# apple1 = Apple("strawbery")
# food1.eat()
# apple1.eat()

# class Animal():
#     # def __init__(self) -> None:
#     def eat(self):
#         print("this animal is eating")
# class Rabbit(Animal):
#     def eat(self):
#         print("this rabbit is eating a corrot")
# rabbit1 = Rabbit()
# rabbit1.eat()

# class A():
#     def do_something():
#         print("From class A")
#         raise NotImplementedError("something went wrong")
# class B(A):
#     def do_something():
#         print("From class B")
# class C(A):
#     pass
# x = B()
# z = C()
# C.do_something()

# class x():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @property
#     def hello(self):
#         return f"hello {self.name}!!"
# one = x("amine",23)
# print(one.hello)

# from abc import ABCMeta, abstractmethod
# class Programming(metaclass=ABCMeta):
#     @abstractmethod
#     def has_oop(self):
#         pass
# class Python(Programming):
#     def has_oop(self):
#         return "yes"
# class Pascal(Programming):
#     def has_oop(self):
#         return "no"
# class Java(Programming):
#     def has_oop(self):
#         return "yes"
# one = Programming()
# two = Python()
# three = Pascal()
# four = Java()
# print(one.has_oop())
# print(two.has_oop())
# print(three.has_oop())
# print(four.has_oop())

# import pyfiglet
# import termcolor
# import colorama
# colorama.init()
# print(termcolor.colored("amine","red"))
# print(pyfiglet.figlet_format("amine"))
# print(termcolor.colored(pyfiglet.figlet_format("amine"),"yellow"))

# from abc import ABCMeta, abstractmethod
# class name(metaclass=ABCMeta):
#     def get_first(self):
#         return f"first name is amine"
#     def get_middle(self):
#         return f"middle name is mohamed"
#     @abstractmethod
#     def get_last(self):
#         pass
# class full_name(name):
#     def get_last(self):
#         return f"last name is sedrata"
# one = full_name()
# print(one.get_first(),one.get_middle(),one.get_last())


# class Node():
# 	def __init__(self,data):
# 		self.data = data
# 		self.ref = None
# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def length(self):
#         x = 0
#         if self.head == None:
#             return int(0)
#         else:
#             temp = self.head
#             while temp is not None:
#                 temp = temp.ref
#                 x += 1
#             return int(x)
#     def is_empty(self):
#         if self.head == None:
#             return True
#         else:
#             return False
#     def PrintLL(self):
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             while self.head is not None:
#                 print(self.head.data,end="  ==>  ")
#                 self.head = self.head.ref
#         print()
#     def Add_at_Begining(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node
#     def Add_at_End(self,data):
#         new_node = Node(data)
#         if not Linked_list().is_empty():
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.ref is not None:
#                 temp = temp.ref
#             temp.ref = new_node
#     def insert(self,data,index):
#         new_node = Node(data)
#         count = 1
#         temp = self.head
#         while temp.ref != None and count < index:
#             temp = temp.ref
#             count += 1
#         else:
#             new_node.ref = temp.ref
#             temp.ref = new_node
#     def Add_to_Empty(self,data):
#         if not Linked_list.is_empty(self):
#             print("linked list is not empty")
#         else:
#             new_node = Node(data)
#             self.head = new_node
#     def Del_at_Begining(self):
#         if Linked_list.is_empty(self):
#             print("linked list is empty")
#         else:
#             temp = self.head
#             self.head = self.head.ref
#             del(temp)
#     def Del_at_End(self):
#         if Linked_list.is_empty(self):
#             print("linked list is empty")
#         elif Linked_list.length(self) == 1:
#             self.head = None
#         else:
#             temp = self.head
#             while temp.ref.ref is not None:
#                 temp = temp.ref
#             temp.ref = None
#     def Del_by_Value(self,value):
#         if Linked_list.is_empty(self):
#             return "linked list is empty"
#         elif self.head.data == value:
#             Linked_list.Del_at_Begining(self)
#         else:
#             temp = self.head
#             while temp.ref is not None:
#                 if temp.ref.data == value:
#                     break
#                 temp = temp.ref
#             if temp.ref is None:
#                 print(f"value {value} not found")
#             else:
#                 temp.ref = temp.ref.ref
    # def Reverse(self):
#         if self.head == None:
#             print("linked list is empty")
#         elif self.head.ref == None:
#             return self.head
#         else:
#             prv,cur,nxt = self.head,self.head.ref,self.head.ref.ref
#             prv.ref = None
#             while nxt is not None:
#                 cur.ref = prv
#                 prv = cur
#                 cur = nxt
#                 nxt = nxt.ref
#             cur.ref = prv
#             self.head = cur

# LL1 = Linked_list()
# LL1.Add_at_Begining(6)
# LL1.PrintLL()
# LL1.Del_by_Value(1)
# LL1.Del_at_End()
# print(LL1.is_empty())
# print(LL1.length())
# LL1.Del_at_Begining()
# LL1.Add_at_End(4)
# LL1.Add_at_Begining(5)
# LL1.insert()
# LL1.Add_to_Empty(7)

# from os import system
# system("cls")

# class aaa:
#     def __init__(self,integer:int):
#         self.integer = integer
#     def __repr__(self):
#         return "__repr__ from aaa"
#     def __str__(self):
#         return "__str__ from aaa"
# class name():
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return "__str__ from {self.__class__.__name__}".format(self=self)
# x = name("amine")
# print(x)

# import csv
# class Item:
#     pay_rate = 80
#     all = []
#     users_num = 0
#     def __init__(self,name,price,quantity):
#         assert price >= 0, f"{price} should be greater than zero"
#         assert quantity >= 0, f"{quantity} should be greater than zero"
#         self.price = price
#         self.quantity = quantity
#         self.name = name
#         Item.all.append(self)
#         Item.users_num += 1

#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
#     @staticmethod
#     def show_num_users():
#         print("number of users is {}".format(Item.users_num))
#     @staticmethod
#     def from_percent(percent):
#         return percent/100
#     def apply_discount(self):
#         self.price *= self.from_percent(self.pay_rate)
#     def calculate_total_price(self):
#         return self.price * self.quantity
#     def instanciate_from_csv():
#         with open("oop.csv","r") as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#             for item in items:
#                 Item(
#                     name=item.get('name'),
#                     price=float(item.get('price')),
#                     quantity=float(item.get('quantity'))
#                 )
# # Item.instanciate_from_csv()
# item1 = Item('phone',33,1)
# # item1.pay_rate = 50
# # item1.apply_discount()
# class phone(Item):
#     def __init__(self,name,price,quantity,year):
#         super().__init__(name,price,quantity)
#         self.year = year
#     def __add__(self,other):
#         if isinstance(other,phone):
#             return self.price + other.price
#         else:
#             return NotImplemented
# my_phone1 = phone("huawei",350,1,2022)
# my_phone2 = phone("redmi",199,1,2018)

# print(Item.all)
# print(phone.all)

# class laptop(Item):
#     def __init__(self,name,price,quantity,CPU):
#         super().__init__(name,price,quantity)
#         self.CPU = CPU
# my_laptop = laptop("lenovo",499,1,"core i5")

# print(my_phone1.__add__(my_phone2))
# print(str.__len__("string"))
# print(my_phone1+my_phone2)

# class Employee():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     @property
#     def email(self):
#         return f"{self.first}.{self.last}@gmail.com"
#     @property
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     @fullname.setter
#     def fullname(self, new_name:str):
#         self.first ,self.last = new_name.split(" ")
#     @fullname.deleter
#     def fullname(self):
#         self.first = None
#         self.last = None
#         print("Name deleted")
# employee1 = Employee("john","clinton")

# employee1.fullname = "john wick"
# del employee1.fullname
# print(employee1.fullname)
# print(employee1.email)
# print(employee1.fullname)

# class x():
#     def __init__(self,name):
#         self.namee = name
    # @property
    # def name(self):
    #     return self.__name
# xxx = x("amine")
# print(xxx.namee) 


# from abc import ABCMeta,abstractmethod
# class person(metaclass=ABCMeta):
#     def imp_method(self):
#         return f"exists in {__class__.__name__}"
#     def unimp_method(self):
#         return f"exists in {__class__.__name__}"
# class man(person):
#     def unimp_method(self):
#         return f"exists in class {__class__.__name__}"
# person1 = person()
# man1 = man()
# print(person1.unimp_method())
# print(person1.imp_method())
# print(man1.unimp_method())
# print(man1.imp_method())

# class person():
#     def __init__(self,firstname,lastname):
#         self.__firstname = firstname
#         self.__lastname = lastname
#     @property
#     def firstname(self):
#         return self.__firstname
#     @firstname.setter
#     def firstname(self,new):
#         self.__firstname = new
# person1 = person("amine","sedrata")
# print(person1.firstname)
# person1.firstname = "main"
# print(person1.firstname)

'the getsource function from the inspect library provides the code writen to create a function or a class'
# from inspect import getsource

# class test:
#     def __init__(self,zen):
#         self.zen = zen
#     def __call__(self):
#         print("i was called")
# test1 = test(3)
# test1()

'meta class'
# from abc import ABCMeta
# from inspect import getsource
# print(getsource(ABCMeta))
# class inherit():
#     def say_hi(self):
#         return "hey you"
# def add_attribute(self):
#     self.z = 9
# TST = type("TST",(inherit,),{"age":20,"name":"amine","gender":"male","add_attribute":add_attribute})
# tst1 = TST()
# print(tst1.say_hi())
# tst1.add_attribute()
# print(tst1.z)

# print(tst1.name)
# print(tst1.age)
# print(f"my name is {tst1.name} i am {tst1.age} yo")

# class Meta(type):
#     def __new__(self,class_name,bases,attrs):
#         print(attrs)
#         a = {}
#         for name,val in attrs.items():
#             if name.startswith("__"):
#                 a[name] = val
#             else:
#                 if isinstance(val,int):
#                     a[name] = val*2
#                 elif isinstance(val,str):
#                     a[name] = val.upper()
#         print(a)
#         return type(class_name,bases,a)
# class dog(metaclass=Meta):
#     num1 = 4
#     num2 = 8
#     name = "amine"
# print(dog.num1,dog.num2,dog.name)

# import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         x = func()
#         total = time.time() - start
#         print("Time: ",total)
#     return wrapper()
# @timer
# def test():
#     for i in range(100000000):
#         pass

# import sys
# def iter(n):
#     for i in range(n):
#         yield i
# lst = [i for i in range(100000)]
# g = iter(100000)
# print(sys.getsizeof(lst))
# print(sys.getsizeof(g))

# lst = ['a day off','analyse','algebra','datastructure']
# from random import randint
# print(lst[randint(0,3)])


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         one = 0
#         two = 1
#         steps = 2
#         while True:
#             if two == len(nums):
#                 one = 0
#                 two = steps
#                 steps+=1
#             if nums[one] + nums[two] == target:
#                 return one,two
#                 break
#             else:
#                 one+=1
#                 two+=1

# number = int(input("enter a number:  "))
# expo = int(input("enter the power number:  "))
# x = number
# for i in range(expo-1):
#     number*=x
# print(number)

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return (num* factorial(num-1))
# print(factorial(5))
# cache = {}
# def fibonacci(index):
#     if index in cache:
#         return cache[index]
#     elif index == 1 or index == 2:
#         value = 1
#         return value
#     else:
#         value = (fibonacci(index-1))+(fibonacci(index-2))
#         if value not in cache:
#             cache[index] = value
#         return value

''' l'intero '''
# num = 0
# while num < 2:
#     num = int(input("enter a number:  "))
# cmt = 2
# somme = 3
# produit = 1
# while cmt <= num:
#     produit *= somme
#     somme += num
#     cmt += 1
# print(f"la valeur de E est:   {produit}")

# from time import time
# from random import randint
# password = 123456789
# given = 0000
# start = time()
# while given != password:
#     given = randint(0,999999999)
# for i in range(999999999):
#     if i == password:
#         given = i
#         break
# end = time()
# print(given)
# print(end-start)

# class Solution():
#     def __init__(self,num):
#         self.num = num
#     def fact(self,fact_num):
#         result = 1
#         for i in range(1,fact_num+1):
#             result *= i
#         return result
#     def sum(self):
#         final = 0
#         for t in range(1,self.num+1):
#             final += self.fact(t+1)
#         return final
# n = int(input("enter a number:  "))
# s = Solution(n)
# print(s.sum())

# def num_rev(number):
#     Rev = 0
#     while number:
#         Rev *= 10
#         Rev += number%10
#         number //= 10
#     return(Rev)

# import itertools
# x = [2,2,2]
# f = ["f","f","s"]
# t = [x,f]
# ziped = [*(itertools.zip_longest(*t))]
# print(ziped)

# 'sorting a dictionary'
# dic = {}
# for i in range(10,0,-1):
#     dic[f"number{11-i}"] = i
# sorted_dic = sorted(dic.items(),key=lambda x:x[1])
# print(sorted_dic)

