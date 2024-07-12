def cube(num):
   return num*num*num
print(cube(5))

def say_hi(name):
   print("hello "+name)
say_hi("bro")

def welcome(name,age):
   print("hello " + name + " you are " + age + " years old")
welcome("amine","20")

def cube(num):
   return num*num*num
def sum(num1,num2):
   return num1+num2
print(sum(55,77))

def match_string(str1, str2):
   if str1 == str2:
       print("the strings do match")
   else:
       print("the strings do not match")
match_string("good morning", "good evening")

def power(num1, num2):
   result = 1
   for x in range(num2):
       result = result * num2
   return result
print(power(5,30))

def say_hi():
    return "hello by python from inside the function"
print(say_hi())

def say_hello(name):
    print(f"hello {name}")
say_hello("amine")
say_hello("sami")
say_hello("mohamed")

sum1 = int(input("enter the first number:    "))
sum2 = int(input("enter the second number:    "))
def addition():
    print(sum1+sum2)
addition()

def say_hi(*peoples):
    for name in peoples:
        print(f"hello {name}")
say_hi("amine", "mina", "sally", "islam")

def introduction (name, age, country = "unknown"):
    print(f"Hello {name} Your Age is {age}, you are from {country}")
introduction("amine", "20")

def add(*sum):
    num = 0
    for i in sum:
        num += i
        result = num
    return num
print(add(1, 1, 4, 5 ,6 ))

skills_with_progress = {
    "php": "70%",
    "css": "60%",
    "ps": "70"
}
def hello(name, *args,**kwargs):
        print(f"hello {name}\nYour Skills Without Progress are :")
        for skill in args:
            print(skill)
        print("your skills with progress are   :")
        for skill_key, skill_value in skills_with_progress.items():
            print(f"{skill_key} ==> {skill_value}")
hello("amine", "python", "JS")

def function():
    global x
    x = 10
    print(f"local x is {x}")
print(f"global x before calling the function is {x}")
function()
print(f"global x is {x}")

def clean_Word(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return clean_Word(word[1:])
    return word[0] + clean_Word(word[1:])
print(clean_Word("eeeeeeeedddddddddiiiiitttttt"))

introduction = lambda name, age : f"hello {name} your age is {age}"
print(introduction("amine", 20))

def check(num):
    if num == 0:
        return True
list_of_nums = [0,52,6,7,5,34,12,5]
x = filter(check, list_of_nums)
for number in x:
    print(number)

def checkName(name):
    return name.startswith("A")
friends = ["Amine","osama","Ahmed","ayman"]
friends_check = filter(checkName,friends)
for friend in friends_check:
    print(friend)

def add(*nums):
    sum = 0
    for index in nums:
        sum += index
    return sum
print(add(78,98,66,9))

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f
print(fact(3))

def say_hi(name) -> str:
    print(f"hello {name}")
say_hi("amine")
def sum(n1,n2) -> int:
    print(n1+n2)
sum("amine","sdrt")

def Serial(count) -> int:
    all_chars = string.ascii_letters + string.digits
    chars_num = len(all_chars)
    serial_list = []
    while count > 0:
        random_num = random.randint(0,chars_num - 1)
        random_char = all_chars[random_num]
        serial_list.append(random_char)
        count -= 1
    print("".join(serial_list))
Serial(20)

def reverse1(given_int):
    x = str(given_int)
    r = reversed(x)
    for i in r:
        print(i,end="")
reverse1(123456789)
def reverse2(given_int):
    x = str(given_int)
    r = x[::-1]
    for i in r:
        print(i,end="")
reverse2(123456789)

def longest_word(sentence):
    max = 0
    for i in splited:
        if len(i) > max:
            max = len(i)
            longest = i
    return longest
print(longest_word("i love pizza"))

def remove(word,letter):
    clean = []
    for i in word:
        if i == letter:
            continue
        clean.append(i)
    print("".join(clean))
remove("it's ok@ay if@ you@ find it hard@ at first" , "@")

def remove(word):
    result = filter(lambda x:x != "@" and x != "#" and x != "3" ,word)
    return "".join(result)
print(remove("3it3#33's ok@a33#y #if3@ 3y##ou@ 33#fi#n3#d #it# 33##ha3r3d@ at 333#f#ir3s3t33#33333"))

def re_duplicated(sentence):
    x = sentence.split(" ")
    result = []
    for i in x:
        if i not in result:
            result.append(i)
    return " ".join(result)
print(re_duplicated("i love web web development"))

def re_duplicated(sentence):
    x = sentence.split(" ")
    result = list(dict.fromkeys(x))
    return " ".join(result)
print(re_duplicated("i love web web development"))

def add_us_and_commas(number):
    string = str(number)
    list_of_nums = []
    count = 0
    for i in string:
        list_of_nums.append(i)
        count +=1
        if count / 3 == 1:
            list_of_nums.append("_")
        elif count / 3 > 1 and count % 3 == 0:
            list_of_nums.append(",")
    return "".join(list_of_nums)
print(add_us_and_commas(797296598687587174))
def add_us_and_commas(number):
    formatted = f"{number:,}"
    if len(formatted) > 3:
        spl = formatted.split(",")
        all_but_last = spl[:-1]
        fjoin = "".join(all_but_last)
        ijoin = int(fjoin)
        return f"{ijoin:,}_{spl[-1]}"
    return formatted
print(add_us_and_commas(797296598687587174))

def series_resistance(nums):
    return "{} ohm{}".format(sum(nums),"s" if sum(nums)>=2 else "")
print(series_resistance([8,8]))

def ds(nums):
    print("{} ohm{}".format(sum(nums),"s" if sum(nums)>=2 else ""))
ds([42,24,41])

def series_resistance(lst):
	total = sum(lst)
	return '{} ohm{}'.format(total, 's' * (total > 1))
print(series_resistance([2,24,41,1]))

def is_curzon(num):
    x = 2 ** num + 1
    y = 2 * num + 1
    if x % y == 0:
        return True
    else:
        return False

def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Can't divide by 0!"
        return num1 / num2

def calculator(n1, operator, n2):
	try: 
		return eval(str(n1)+operator+str(n2))
	except ZeroDivisionError:
		return "Can't divide by 0!"
print(calculator(2,"*",5))

def factorial(num):
    if num >= 0:
        neg_one = num - 1
        while neg_one > 1:
            num *= neg_one
            neg_one -= 1
        return num
print(factorial(0))

def dis(price, discount):
    x = (discount/100)*price
    result = price - x
    return round(result,2)

def is_triplet(n1, n2, n3):
    x = max(n1,n2,n3)**2
    z = (n1**2+n2**2+n3**2)-x
    if x == z:
        return True
    else:
        return False

def damage(damage, speed, time):
    if damage < 0 or speed < 0:
        return "invalid"
    x = damage*speed
    if time == "second":
        return x
    elif time == "minute":
        return x*60
    elif time == "hour":
        return x*3600

def damage(damage, speed, time):
	secs = {'second':1, 'minute':60, 'hour':3600}
	ans = damage*speed*secs[time]
	return ans if ans>0 and speed>0 else 'invalid'

def counterpartCharCode(char):
    if char.isupper():
        return ord(char.lower())
    else:
        return ord(char.upper())

def counterpartCharCode(char):
	return ord(char.swapcase())
print(counterpartCharCode("a"))

def to_camel_case(text):
    for i in text:
        if i == "-"
            index = index(text,"-")

to_camel_case("jlkf")
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result
def unique_in_order(iterable):
    newList = []
    for item in iterable:
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    return newList
print(unique_in_order('AAAABBBCCDAABBB'))

def is_square(n):
    if n < 0 or str(n**0.5).split(".")[1] != "0":
        return False
    else:
        return True

def unique_in_order(iterable):
    newlist = []
    for i in iterable:
        if len(newlist) == 0 or i != newlist[len(newlist)-1]:
            newlist.append(i)
    return newlist
print(unique_in_order('AAAABBBCCDAABBB'))

def dig_pow(n, p):
    newlist = []
    for i in str(n):
        newlist.append(int(i)**p)
        p += 1
        final = str((sum(newlist))/n).split(".")
    if final[1] == "0":
        return final[0]
    else:
        return -1

def dig_pow(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1

def cakes(recipe, available):
    list_of_num = []
    list_of_str = []
    result = []
    x = 0
    for i,n in recipe.items():
        list_of_num.append(n)
        list_of_str.append(i)
    z = len(list_of_num)
    for a,b in available.items():
        list_of_num.append(b)
        list_of_str.append(a)
    if z > len(list_of_num)-z:
        return 0
    while len(list_of_num)-1 > z:
        result.append(list_of_num[z]/list_of_num[x])
        x += 1
        z += 1

def soc(y,x=1):
    return x + y
print(soc(8,3))

def reverse(string):
    a = []
    if string == "":
        return a
    a.append(string[len(string)-1])
    reverse(string[:-1])
print(reverse("hellothere"))