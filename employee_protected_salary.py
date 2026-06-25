# Create an Employee class with a protected attribute _salary.
# Use a method to print:
# "High Salary" if _salary > 30000
# "Normal Salary" if _salary ≤ 30000

class Employee:
    def __init__(self, salary):
        self._salary= salary

    def salary_status(self):
        if self._salary > 30000:
            return 'High Salary'

        else:
            return 'Normal Salary'

e= Employee(float(input()))
print(e.salary_status())
