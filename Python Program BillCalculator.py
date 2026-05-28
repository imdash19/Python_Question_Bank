# Create a class named BillCalculator with a method calculate_bill().
# If only the price is passed to the method, display the price.
# If price and quantity are passed, calculate and display the total bill amount.

class BillCalculator:
    def calculate_bill(self, price, quantity=None):
        if quantity is None:
            print(price)
        else:
            print(price * quantity)

b = BillCalculator()

n = int(input())

if n == 1:
    price = int(input())
    b.calculate_bill(price)

elif n == 2:
    price = int(input())
    quantity = int(input())
    b.calculate_bill(price, quantity)
