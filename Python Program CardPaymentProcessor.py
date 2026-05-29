# Create a parent class Payment with method pay(amount). 
# Create a child class CardPayment that overrides pay() to add 2 percent service charge.

class Payment:
    def pay(self, amount):
        print(f"{amount:.2f}")

class CardPayment(Payment):
    def pay(self, amount):
        final_amount = amount + (amount * 2 / 100)
        print(f"{final_amount:.2f}")

amount = float(input())

c = CardPayment()
c.pay(amount)
