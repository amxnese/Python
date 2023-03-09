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
# time.sleep(10)

# class Skill:
#     def __init__(self):
#         self.skills = ["css, java, python"]
#     def __str__(self):
#         return f"my skills are {self.skills}"
#     def __len__(self):
#         return len(self.skills)
# print(len(Skill()))
# print(Skill())




