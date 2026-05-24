# Create a base class Account with method get_balance().
# Create child classes SavingsAccount and CurrentAccount.
# SavingsAccount adds 5 percent interest. CurrentAccount adds no interest.

class Account:
    def get_balance(self):
        self.balance = int(input())

class SavingsAccount(Account):
    def add_interest(self):
        print(self.balance + (self.balance * 5 // 100))

class CurrentAccount(Account):
    def add_interest(self):
        print(self.balance)

s = SavingsAccount()
s.get_balance()
s.add_interest()

c = CurrentAccount()
c.get_balance()
c.add_interest()