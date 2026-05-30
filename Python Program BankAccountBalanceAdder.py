# Create a class BankAccount with attribute balance. 
# Overload the + operator using __add__() to calculate total balance of two accounts.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

balance1 = float(input())
balance2 = float(input())

account1 = BankAccount(balance1)
account2 = BankAccount(balance2)

print(f"{account1 + account2:.2f}")
