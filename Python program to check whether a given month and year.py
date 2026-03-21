# Write a Python program to check whether a given month and year contains a Monday 13th.
# Month No.: 11 Year: 2022
# Check whether the said month and year contains a Monday 13th.: False
# Month No.: 6 Year: 2022
# Check whether the said month and year contains a Monday 13th.: True

import datetime

m = int(input())
y = int(input())

d = datetime.date(y, m, 13)

print(d.weekday() == 0)