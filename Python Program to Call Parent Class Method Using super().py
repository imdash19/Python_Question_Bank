# Create a parent class Bank with a method interest() that prints "Base Interest Rate".
# Create a child class SBI.
# Inside the child class, create a method show_interest() and call the parent class method using super().interest().

class Bank:
    def interest(self):
        print("Base Interest Rate")

class SBI(Bank):
    def show_interest(self):
        super().interest()

s = SBI()
s.show_interest()
