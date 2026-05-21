#Create a class Cart with method get_total(). 
#Create another class Discount with method apply_discount(). 
#Create a child class Checkout that applies 10 percent discount if cart total exceeds 1000.

class Cart:
    def get_total(self):
        self.total = int(input())

class Discount:
    def apply_discount(self):
        if self.total > 1000:
            print(self.total - (self.total * 10 // 100))
        else:
            print(self.total)

class Checkout(Cart, Discount):
    pass

c = Checkout()
c.get_total()
c.apply_discount()
