from abc import ABCMeta,abstractmethod
class person(metaclass=ABCMeta): # Serves as a Blueprint To its Sub Classes
    @abstractmethod
    def status(self):
        pass
class man(person):
    def status(self): # obligated to implement
        return "ok"
    def gender(self):
        return "male"
    
man1 = man()
print(man1.status()) # ok
