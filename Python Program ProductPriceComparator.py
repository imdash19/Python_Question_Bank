# Create a class Product with attribute price. 
# Overload the < operator using __lt__() to compare prices of two products.

class Product:
    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

price1 = float(input())
price2 = float(input())

product1 = Product(price1)
product2 = Product(price2)

print(product1 < product2)
