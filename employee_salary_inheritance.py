# Create a parent class Employee that stores an employee’s salary.
# Create a child class that inherits from Employee.
# Use the super() method to access the salary from the parent class.

# Based on the salary value, display the salary status.

# Salary Conditions

# If salary is greater than 30000, display “High Salary”
# If salary is less than 30000, display “Normal Salary”

class Employee:
    def __init__(self, salary):
        self.salary= salary

class Child(Employee):
    def __init__(self, salary):
        super().__init__(salary)

    def status(self):
        if self.salary > 30000:
            print("High Salary")
        else:
            print("Normal Salary")

c= Child(float(input()))
c.status()
