class Writer:
    def __init__(self, name):
        self.__name = name
        self.__tool = None
    # Getter

    @property
    def name(self):
        return self.__name
    # Getter

    @property
    def toll(self):
        return self.__toll
    # Setter

    @toll.setter
    def toll(self, tool):
        self.__toll = tool


class Pen:
    def __init__(self, brand):
        self.__brand = brand
    # Getter

    @property
    def brand(self):
        return self.__brand

    @property
    def write(self):
        print('Pen is wirte...')


class Typewriter:
    def write(self):
        print('Typerwriter is write...')
