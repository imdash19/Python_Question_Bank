# You need to create a program that calculates the final amount for different types of orders.
# There are two types of orders:

# NormalOrder: The final amount is the same as the order amount (no extra charges).
# ExpressOrder: If the order amount is less than 1000, a delivery charge of 100 is added. If the amount is 1000 or more, no delivery charge is added.

# Input Format:

# First line: Order type (either "Normal" or "Express")
# Second line: Order amount (a number)

# Output Format:

# Print the final amount (rounded to 2 decimal places)

class Order:
    def get_amount(self):
        self.amount = float(input())

class NormalOrder(Order):
    def final_amount(self):
        print(f"{self.amount:.2f}")

class ExpressOrder(Order):
    def final_amount(self):
        if self.amount < 1000:
            self.amount += 100
        print(f"{self.amount:.2f}")

order_type = input()

if order_type == "Normal":
    o = NormalOrder()
else:
    o = ExpressOrder()

o.get_amount()
o.final_amount()
