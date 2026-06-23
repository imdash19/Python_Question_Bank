# Create an Employee class with a parameterized constructor.
# The constructor should accept salary and print:
# "High Salary" if salary > 30000
# "Normal Salary" if salary ≤ 30000

class Employee:
    def __init__(self, salary):
        self.salary= salary

e= Employee(float(input()))

if e.salary > 30000:
    print("High Salary")

else:
    print("Normal Salary")
