# You need to create a program that calculates electricity bills for different types of connections.
# There are two types of electricity connections:

# Domestic: The rate is 3 rupees per unit of electricity consumed.
# Commercial: The rate is 5 rupees per unit of electricity consumed.

# Input Format:

# First line: Connection type (either "Domestic" or "Commercial")
# Second line: Number of units consumed (a number)

# Output Format:

# Print the total bill amount (rounded to 2 decimal places)

class ElectricityBillGenerator:
    def calculate_bill(self, connection_type, units):
        if connection_type == "Domestic":
            bill = units * 3
        elif connection_type == "Commercial":
            bill = units * 5

        print(f"{bill:.2f}")

connection_type = input()
units = float(input())

e = ElectricityBillGenerator()
e.calculate_bill(connection_type, units)
