from abc import ABCMeta,abstractmethod
class person(metaclass=ABCMeta):
    @abstractmethod
    def status(self):
        pass
class man(person):
    def status(self):
        return "ok"
    def gender(self):
        return "male"
one = man()
print(one.gender())
