# Perfect! Let me create the beginner-friendly version:

# 1. Problem Statement Description
# You need to create a program that calculates the final balance of a savings account after applying interest.
# The program should:

# Take the account balance as input
# Calculate interest at 5% per year on the balance
# Add the interest to the balance only if the balance is greater than 1000
# If the balance is 1000 or less, no interest is added

# Input Format:

# Single line: Account balance (a number)

# Output Format:

# Print the final balance after adding interest (if applicable), rounded to 2 decimal places

class SavingsInterestCalculator:
    def calculate_balance(self, balance):
        if balance > 1000:
            balance += balance * 0.05

        print(f"{balance:.2f}")

balance = float(input())

s = SavingsInterestCalculator()
s.calculate_balance(balance)
