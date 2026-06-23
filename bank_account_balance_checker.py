# Create BankAccount class with balance attribute and print Sufficient Balance if >=500

class BankAccount:
    def __init__(self, balance):
        self.balance= balance

account= BankAccount(float(input()))

if account.balance >= 500:
    print('Sufficient Balance')

else:
    print('Low Balance')
