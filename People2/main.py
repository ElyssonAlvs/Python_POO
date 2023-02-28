from datetime import datetime
from random import randint


class People:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_year_of_bith(self):
        print(self.current_year - self.age)
    """
    a function without dependence on the content of an object 
    or the execution of an instance of a class, being able to 
    directly call any method of the class and also manipulate 
    some fields of the class
    """
    @classmethod
    def by_birth_year(cls, name, year_of_birth):
        age = cls.current_year - year_of_birth
        return cls(name, age)
    """
    independent methods of the class, do not need instance,
    functioning as a function within the class;
    """
    @staticmethod
    def creat_ID():
        rand = randint(10000, 19999)
        return rand


# Test 1
"""
p1 = People('Luiz', 32)
print(p1)
print(p1.name, p1.age)
p1.get_year_of_bith()

"""
# Test 2
p1 = People.by_birth_year('Luiz', 1987)
print(p1)
print(p1.name, p1.age)
p1.get_year_of_bith()
print(People.creat_ID())
print(p1.creat_ID())
