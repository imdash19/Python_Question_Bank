# Create a class Income with method get_income(). 
# Create another class Tax with method calculate_tax(). 
# Create a child class Employee that deducts tax only if income exceeds 25000.

class Income:
    def get_income(self):
        self.income = int(input())

class Tax:
    def calculate_tax(self):
        if self.income > 25000:
            print(self.income - (self.income * 10 // 100))
        else:
            print(self.income)

class Employee(Income, Tax):
    pass

e = Employee()
e.get_income()
e.calculate_tax()
