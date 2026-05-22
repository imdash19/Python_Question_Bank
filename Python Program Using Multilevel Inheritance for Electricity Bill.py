# Design a program using Multilevel Inheritance:
# Create base class Meter with method get_units(). 
# Create child class BillCalculator that calculates bill amount. 
# Create another child class FinalBill that applies 5 percent discount if units are below 100.

class Meter:
    def get_units(self):
        self.units = int(input())

class BillCalculator(Meter):
    def calculate_bill(self):
        self.bill = self.units * 10

class FinalBill(BillCalculator):
    def final_amount(self):
        if self.units < 100:
            print(self.bill - (self.bill * 5 // 100))
        else:
            print(self.bill)

f = FinalBill()
f.get_units()
f.calculate_bill()
f.final_amount()