# Create a BankAccount class with a constructor.
# The constructor should accept balance and print:
# "Sufficient Balance" if balance ≥ 500
# "Low Balance" if balance < 500

class BankAccount:
    def __init__(self, balance):
        self.balance= balance

b= BankAccount(float(input()))

if b.balance >= 500:
    print("Sufficient Balance")

else:
    print("Low Balance")
