# Write a Python program to calculate the number of days between two dates.
# Sample dates: (2014, 7, 2), (2014, 7, 11)
# Expected output: 9 days

from datetime import date

# Input for first date
y1 = int(input("Enter year (start date): "))
m1 = int(input("Enter month (start date): "))
d1 = int(input("Enter day (start date): "))

# Input for second date
y2 = int(input("\nEnter year (end date): "))
m2 = int(input("Enter month (end date): "))
d2 = int(input("Enter day (end date): "))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

difference = abs((date2 - date1).days)

print("\nDifference:", difference, "days")