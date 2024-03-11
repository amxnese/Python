

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

# from random import randint
# print(randint(0,10))

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


# test.assert_equals(make_readable(0), "00:00:00")
# test.assert_equals(make_readable(5), "00:00:05")
# test.assert_equals(make_readable(60), "00:01:00")
# test.assert_equals(make_readable(86399), "23:59:59")
# test.assert_equals(make_readable(359999), "99:59:59")



# def soc(y,x=1):
#     return x + y
# print(soc(8,3))

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

# def solution(number):
#     return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])

# def zeros(n):
#     x = n/5
#     return x+zeros(x) if x else 0
# print(zeros(646464))

# for i in range(0,11):
#     if i%2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")


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
#     if  len(s) < 2:
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

'''the getsource function from the inspect library provides the code writen
to create a function or a class'''
# from inspect import getsource

# Reversing a Number
# def num_rev(number):
#     Rev = 0
#     while number:
#         Rev *= 10
#         Rev += number%10
#         number //= 10
#     return(Rev)

