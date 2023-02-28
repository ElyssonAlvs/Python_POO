"""
ELYBANK 2.0 😀 with POO
The __new__() method is actually the constructor and is actually creating a
Account instance. The __init__() method is responsible for initializing the object, so much so that already
takes the instance (self) created by the constructor as an argument

O método __init__() é responsável por inicializar o	objeto, tanto é	 que já recebe a própria	
instância (self) criada	pelo construtor	como argumento.

Como o self é a referência do objeto, ele chama self.titular e self.saldo da classe Conta.

Since self is the object's reference, it calls self.holder and self.balance from the Account class. 

Método que seja	chamado via classe e via instância sem a necessidade de passar a referência
deste objeto. O Python resolve isso usando métodos estáticos.

Method that is called via class and via instance without the need to pass the reference
of this object. Python solves this using static methods.
"""
import datetime


class InsufficientBalanceError(RuntimeError):
    pass


class TaxableMixIn:
    def get_impost_value(self):
        pass


class Historic:
    def __init__(self):
        self.open_date = datetime.datetime.today()
        self.transactions = []

    def prints(self):
        print('Open date : {}'.format(self.open_date))
        print('Trasactions : ')
        for t in self.transactions:
            print('-', t)


class Client:
    def __init__(self, name, surname, cpf):
        self.name = name
        self.surname = surname
        self.cpf = cpf


class Account:
    def __init__(self,	number,	holder,	balance, limit=1000.0):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit
        self.historic = Historic()

    def deposit_money(self, value):
        self.balance += value
        self.historic.transactions.append('Deposit of {}'.format(value))

    def withdraw_money(self, value):
        if (self.balance < value):
            print('is not possible withdraw money off limit')
            return False
        else:
            self.balance -= value
            self.historic.transactions.append('Withdrawal of {}'.format(value))

    def extract_account(self):
        print('Number : {}\nBalance : {}'.format(self.number, self.balance))
        self.historic.transactions.append(
            'Took extract - balance of {}'.format(self.balance))

    def transfer_money(self, destiny, value):

        withdrew = self.withdraw_money(value)
        if (withdrew == False):
            return False
        else:
            destiny.deposit_money(value)
            self.historic.transactions.append(
                'Transfer of {} from account {}'.format(value, destiny.number))
            return True

    def actualize(self, taxa):
        self.balance += self.balance * taxa

    def __str__(self):
        return f'Data of Account: \nNumber: {self.number} \nHolder: {self.holder} \nBalance: {self.limit} \nLimit: {self.balance}'


class Account_updater:

    def __init__(self, selic, total_balance):
        self._selic = selic
        self._total_balance = total_balance

        def run(self):
            print(f'Account Balance: {Account.balance}')
            self._total_balance += Account.actualize(self._selic)
            print(f'Final Balance: {self.total_balance}')


class Current_account(Account, TaxableMixIn):
    def actualize(self, taxa):
        self.balance += self.balance * taxa * 2

    def deposit(self, value):
        self.saldo += value - 0.1

    def get_impost_value(self):
        return self._balance * 0.01

    def withdraw_money(self, value):
        if(value < 0):
            raise ValueError('tried to withdraw a negative value')
        if (self._balance < value):
            raise InsufficientBalanceError('Insufficient Balance')
        self._balance -= (value + 0.10)


class Savings_account:
    def actualize(self, taxa):
        self.balance += self.balance * taxa * 3


class Life_insurance(TaxableMixIn):
    def __init__(self, value, holder, number_tax):
        self._value = value
        self._holder - holder
        self._number_tax = number_tax

    def get_impost_value(self):
        return 50 + self._value * 0.05


class Tax_handler:
    def impost_calc(self, list_taxable):
        total = 0
        for t in list_taxable:
            total += t.get_impost_value()
        return total
