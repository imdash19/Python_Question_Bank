# You need to create a program that determines whether an employee is eligible for leave based on their attendance percentage.
# The program should:

# Take the employee's attendance percentage as input
# Check if the attendance is greater than or equal to 75%
# Print "Eligible" if attendance is 75% or more
# Print "Not Eligible" if attendance is less than 75%

# Input Format:

# Single line: Attendance percentage (a number)

# Output Format:

# Print either "Eligible" or "Not Eligible"

class EmployeeLeaveEligibility:
    def check_eligibility(self, attendance):
        if attendance >= 75:
            print("Eligible")
        else:
            print("Not Eligible")

attendance = float(input())

e = EmployeeLeaveEligibility()
e.check_eligibility(attendance)
