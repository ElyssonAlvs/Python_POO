from datetime import datetime


class People:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def speak(self, subject):
        if self.eating:
            print(f'{self.name}can not talk while eating.')
            return
        if self.talking:
            print(f'{self.name} is already talking.')
            return

        print(f'{self.name} is talking to {subject}')
        self.talking = True

    def stop_speak(self):
        if not self.talking:
            print(f'{self.name} is not talking.')
            return

        print(f'{self.name} stopped talking.')
        self.talking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating.')
        if self.talking:
            print(f'{self.name} can not talk while eat')
            return

        print(f'{self.name} is eat a {food}.')
        self.eating = True

    def stop_eat(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return
        print(f'{self.name} stop eating.')
        self.eating = False

    def get_current_year(self):
        return self.current_year - self.age
