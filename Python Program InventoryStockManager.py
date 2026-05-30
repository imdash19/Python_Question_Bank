# Create a class Inventory with attribute stock. 
# Overload the - operator using __sub__() to subtract sold items from available stock.

class Inventory:
    def __init__(self, stock):
        self.stock = stock

    def __sub__(self, other):
        return self.stock - other.stock

available_stock = int(input())
sold_items = int(input())

inventory = Inventory(available_stock)
sold = Inventory(sold_items)

print(inventory - sold)
