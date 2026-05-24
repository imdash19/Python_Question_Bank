# Create base class Cart with method get_price(). 
# Create child class TaxCalculator that adds 10 percent tax. 
# Create another child class Checkout that applies 5 percent discount if total exceeds 1000.

class Cart:
    def get_price(self):
        self.price = int(input())

class TaxCalculator(Cart):
    def add_tax(self):
        self.total = self.price + (self.price * 10 // 100)

class Checkout(TaxCalculator):
    def final_amount(self):
        if self.total > 1000:
            print(self.total - (self.total * 5 // 100))
        else:
            print(self.total)

c = Checkout()
c.get_price()
c.add_tax()
c.final_amount()
