# Create a Mobile class with attributes model and price then create object and display values

class Mobile:
    def __init__(self, model, price):
        self.model= model
        self.price= price

m= Mobile(input(), int(input()))
print(m.model)
print(m.price)
