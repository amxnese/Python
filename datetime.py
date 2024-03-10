import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.min)
print(datetime.datetime.max)
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)
print(datetime.time.min)
print(datetime.time.max)
print(datetime.datetime(2002,4,6))
print(datetime.datetime(2002,4,6,5,55,33,83976))

BirthYear = int(input("What year have you been born?:   "))
BirthMonth = int(input("What month have you been born?:   "))
BirthDay = int(input("What day have you been born?:   "))
birthday = (datetime.datetime(BirthYear,BirthMonth,BirthDay))
DateNow = datetime.datetime.now()
DaysLived = (f"{(DateNow - birthday).days}")
print(f"You've been alive for {DaysLived} days")

birthday = datetime.datetime(2002,4,6)
print(birthday.strftime)

MyBirthday = datetime.datetime(2002,4,6)
print(MyBirthday)
print(MyBirthday.strftime("%B"))
print(MyBirthday.strftime("%a"))       #this is the same
print(f"{MyBirthday:%a}")              #as this
print(MyBirthday.strftime("%A"))
print(MyBirthday.strftime("%w"))
print(MyBirthday.strftime("%d"))
print(MyBirthday.strftime("%-d"))
print(MyBirthday.strftime("%b"))
print(MyBirthday.strftime("%m"))
print(MyBirthday.strftime("%-b"))
print(MyBirthday.strftime("%I"))

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.min)
print(datetime.datetime.max)
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)
print(datetime.time.min)
print(datetime.time.max)
print(datetime.datetime(2002,4,6))
print(datetime.datetime(2002,4,6,5,55,33,83976))

def make_readable(seconds):
    if seconds < 60:
        return str(datetime.time(0,0,seconds))
    elif seconds < 3600:
        min1 = (int(seconds/60))
        return str(datetime.time(0,min1,seconds%60))
    elif seconds <= 86399:
        hours = (int(seconds/3600))
        min = int((seconds%3600)/60)
        sec = int(((seconds%3600)%60))
        return str(datetime.time(hours,min,sec))
    elif seconds <= 359999:
        hours1 = (int(seconds/3600))
        min2 = int((seconds%3600)/60)
        sec1 = int(((seconds%3600)%60))
        if min2<10:
            min2=f'0{min2}' 
        if sec1<10:
            sec1=f'0{sec1}'
        return f"{hours1}:{min2}:{sec1}"

def make_readable(s):  
    return f'{s // 3600:02}:{s // 60 % 60:02}:{s % 60:02}'

a = datetime.date(2000,1,1)
b = datetime.timedelta(100)
print(a+b)

a = int(input("insert the year you were born in:  "))
b = int(input("insert the month you were born in:  "))
c = int(input("insert the day you were born in:   "))
d = int(input("insert the year you're in:  "))
e = int(input("insert the month you're in:  "))
f = int(input("insert the day you're in:   "))
birthday = datetime.date(a,b,c)
today = datetime.date(d,e,f)
age = (today - birthday).days
if age/30/12 > 18:
    print("you're an adult")
else:
    print("you're a mineur")