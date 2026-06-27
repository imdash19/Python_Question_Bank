# Create a BankAccount class with attributes account_number and balance then create object and print them

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number= account_number
        self.balance= balance

b= BankAccount(int(input()), float(input()))
print(b.account_number)
print(b.balance)
