"""
public, protected, private
_ privado / protected(public_)
__ private (_NAMECLASS__nameatribute)
"""


class DataBase:
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data

    def insert_customer(self, id, name):
        if 'clients' not in self.__data:
            self.__data['clients'] = {id: name}
        else:
            self.__data['clients'].update({id: name})

    def client_list(self):
        for id, name in self.__data['clients'].items():
            print(id, name)

    def delete_client(self, id):
        del self.__data['clients'][id]


# Test 1
"""
bd = DataBase()
bd.insert_customer(1, 'John')
bd.insert_customer(2, 'Elizabeth')
bd.insert_customer(3, 'Rose')
bd.delete_client(2)
bd.client_list()
"""
# Test 2
bd = DataBase()
bd.insert_customer(1, 'John')
bd.insert_customer(2, 'Rose')
print(bd.data)
