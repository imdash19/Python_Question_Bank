# You need to create a program that calculates electricity bills for different types of connections.
# There are two types of electricity connections:

# Domestic: The rate is 3 rupees per unit of electricity consumed.
# Commercial: The rate is 5 rupees per unit of electricity consumed.

# Input Format:

# First line: Connection type (either "Domestic" or "Commercial")
# Second line: Number of units consumed (a number)

# Output Format:

# Print the total bill amount (rounded to 2 decimal places)

class Connection:
    def get_units(self):
        self.units = float(input())

class Domestic(Connection):
    def calculate_bill(self):
        print(f"{self.units * 3:.2f}")

class Commercial(Connection):
    def calculate_bill(self):
        print(f"{self.units * 5:.2f}")

connection_type = input()

if connection_type == "Domestic":
    c = Domestic()
else:
    c = Commercial()

c.get_units()
c.calculate_bill()
