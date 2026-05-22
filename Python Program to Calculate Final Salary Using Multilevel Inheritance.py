# Create base class Employee with method get_salary(). 
# Create child class Bonus that calculates bonus of 10 percent. 
# Create another child class FinalSalary that adds bonus only if salary is above 20000.

class Employee:
    def get_salary(self):
        self.salary = int(input())

class Bonus(Employee):
    def calculate_bonus(self):
        self.bonus = self.salary * 10 // 100

class FinalSalary(Bonus):
    def final_amount(self):
        if self.salary > 20000:
            print(self.salary + self.bonus)
        else:
            print(self.salary)

f = FinalSalary()
f.get_salary()
f.calculate_bonus()
f.final_amount()