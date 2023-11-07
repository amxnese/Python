'meta class'
from abc import ABCMeta
from inspect import getsource
print(getsource(ABCMeta))
class inherit():
    def say_hi(self):
        return "hey you"
def add_attribute(self):
    self.z = 9
TST = type("TST",(inherit,),{"age":20,"name":"amine","gender":"male","add_attribute":add_attribute})
tst1 = TST()
print(tst1.say_hi())
tst1.add_attribute()
print(tst1.z)

print(tst1.name)
print(tst1.age)
print(f"my name is {tst1.name} i am {tst1.age} yo")

class Meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)
        a = {}
        for name,val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                if isinstance(val,int):
                    a[name] = val*2
                elif isinstance(val,str):
                    a[name] = val.upper()
        print(a)
        return type(class_name,bases,a)
class dog(metaclass=Meta):
    num1 = 4
    num2 = 8
    name = "amine"
print(dog.num1,dog.num2,dog.name)