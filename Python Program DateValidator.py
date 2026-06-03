# Reads three integers representing day, month, and year components of a date. The program validates the components form a valid date and may perform additional date logic.

from datetime import datetime

day = int(input())
month = int(input())
year = int(input())

try:
    datetime(year, month, day)
    print("Valid Date")
except ValueError:
    print("Invalid Date")