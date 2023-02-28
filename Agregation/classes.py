class Shopping_cart:
    def __init__(self):
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def product_list(self):
        for product in self.products:
            print(product.name, product.value)

    def total_sum(self):
        total = 0
        for product in self.products:
            total += product.value
        return total


class Product:
    def __init__(self, name, value):
        self.name = name
        self.value = value
