# Coding a Market
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discont(self, percentage):
        self.price = self.price - (self.price * (percentage / 100))
    # Getter 
    @property
    def name(self):
        return self.name
    # Setter
    @name.price
    def name(self, value):
        # First letters capitalized
        self._name = value.title()

    # Getter
    @property
    def price(self):
        return self._price
    
    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            # Replace, Swap what's before the comma for what's after
            value = float(value.replace('R$', ''))
        self._price = value


p1 = Product('Shirt', 50)
p1.discont(10)
print(p1.price)

p2 = Product('Mug', 'R$15')
p2.discont(10)
print(p2.price)
