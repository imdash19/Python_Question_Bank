# This program demonstrates single inheritance and how a child class can reuse parent class functionality.
# Create a parent class BankAccount with a method show_balance() that prints the balance.
# Create a child class SavingsAccount that inherits from BankAccount.
# Accept the balance from the user.

# Create a SavingsAccount object and call show_balance() using the child object.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(self.balance)

class SavingsAccount(BankAccount):
    pass

s = SavingsAccount(int(input()))
s.show_balance()
