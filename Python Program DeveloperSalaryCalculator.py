# Create a parent class Employee with a method calculate_salary(basic).
# Create a child class Developer that overrides calculate_salary() to add a 20% bonus to the basic salary.

class Employee:
    def calculate_salary(self, basic):
        print(basic)

class Developer(Employee):
    def calculate_salary(self, basic):
        salary = basic + (basic * 20 / 100)
        print(f"{salary:.2f}")

basic = float(input())

d = Developer()
d.calculate_salary(basic)
