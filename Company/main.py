# Coding a interprise
import abc


class Authenticated(abc.ABC):
    """
    Abstract class that contains operations of an authenticated object.
    Concrete subclasses must override authenticate method
    """
    @abc.abstractmethod
    def authentic(self, password):
        """
        Abstract method that does password checking.
        Returns True if the password matches, and False otherwise.
        """
        if self._password == password:
            print('Open Access 😀.')
            return True
        else:
            print('Access denied 🤨.')
            return False


class Functionary(abc.ABC):
    def __init__(self, name, cpf, salary=0):
        self._name = name
        self._cpf = cpf
        self._salary = salary

    @abc.abstractmethod
    def get_bonus(self):
        pass


class Manager(Functionary, Authenticated):
    def __init__(self, name, cpf, salary, password, n_subordinates):
        # Functionary.__init__(name, cpf, salary)
        super().__init__(name, cpf, salary)
        self._password = password
        self._n_subordinates = n_subordinates

    def get_bonus(self):
        return self._salary * 0.15

    def authentic(self, password):
        if self._password == password:
            print('Open Access 😀.')
            return True
        else:
            print('Access denied 🤨.')
            return False


class BonusesControl:
    def __init__(self, total_bonuses=0):
        self._total_bonuses = total_bonuses

    def register(self, obj):
        if(hasattr(obj, 'get_bonuses')):
            self._total_bonuses += Functionary.get_bonus()
        else:
            print(
                f'instance of {self.__class__.__name__} does not implement the method get_bonus')
    # Getter

    @property
    def total_bonus(self):
        return self._total_bonuses


class Client(Authenticated):
    def __int__(self, name, cpf, password):
        self._name = name
        self.cpf = cpf
        self._password = password


class Director(Functionary, Authenticated):
    def __init__(self, name, cpf, salary):
        super().__init__(name, cpf, salary)


class Intern_system:
    def login(self, obj):
        if (hasattr(obj, 'authentic')):
            obj.authentic()
            return True
        else:
            print(f'{self.__class__.__name__} is not autheticated.')


# Test 1
"""
manager = Manager('José', '222222222-22', 5000.0, '123-4', 0)
print(manager.get_bonus())
"""

# 500.0

# ----------------------------------------------------------------
# Test 2
"""
functionary = Functionary('João', '111111111-11', 2000.0)
print(vars(functionary))

manager = Manager('José', '222222222-22', 5000.0, '123-4', 0)
print(vars(manager))
"""
# -----------------------------------------------------------------
# Test 3
"""

if __name__ == '__main__':
    functionary = Functionary('John', '111111111-11', 2000.0)
    print(f'Bonus Functionary: {functionary.get_bonus()}')

    manager = Manager('Joe', '222222222-22', 5000.0, '1234', 0)
    print(f'Bonus Manager: {manager.get_bonus()}')

    control = BonusesControl()
    control.register(functionary)
    control.register(manager)

    print(f'Total: {control._total_bonuses}')
"""

# Bonus Functionary: 200.0
# Bonus Manager: 1500.0
# Total: 1700.0

# -------------------------------------------------------------------
# Test 4
director = Director('John', '111111111-11', 4000.0)
''' get_bonus() method mandatory for every object
    which is a subclass of Employee

    Abstract method
 '''
