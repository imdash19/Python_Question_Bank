# You need to create a program that calculates bonuses for employees based on their job type and salary.
# There are two types of employees:

# Manager: Gets a bonus of 10% of salary if their salary is more than 30,000. Otherwise, no bonus.
# Clerk: Gets a bonus of 5% of salary if their salary is more than 20,000. Otherwise, no bonus.

# Input Format:

# First line: Employee type (either "Manager" or "Clerk")
# Second line: Employee salary (a number)

# Output Format:

# Print the bonus amount (rounded to 2 decimal places)

class EmployeeBonusCalculator:
    def calculate_bonus(self, employee_type, salary):
        bonus = 0

        if employee_type == "Manager":
            if salary > 30000:
                bonus = salary * 0.10

        elif employee_type == "Clerk":
            if salary > 20000:
                bonus = salary * 0.05

        print(f"{bonus:.2f}")

employee_type = input()
salary = float(input())

e = EmployeeBonusCalculator()
e.calculate_bonus(employee_type, salary)
