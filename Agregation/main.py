"""
Agregação, uma classe que usa outra classe como parte de si, sendo que essa classe precisa da outra.

Aggregation, a class that uses another class as part of itself, and that class needs the other.
"""
from classes import Shopping_cart, Product

cart = Shopping_cart()
p1 = Product('Shirt', 50)
p2 = Product('iPhone', 10000)
p3 = Product('Hat', 15)
cart.insert_product(p1)
cart.insert_product(p2)
cart.insert_product(p3)

cart.product_list()
print(cart.total_sum())
