# Create a class WorkHours with an attribute hours.
# Overload the * (multiplication) operator using the __mul__() method to calculate the total working hours for a given number of days.

class WorkHours:
    def __init__(self, hours):
        self.hours = hours

    def __mul__(self, days):
        return self.hours * days

hours = int(input())
days = int(input())

work = WorkHours(hours)

print(work * days)
