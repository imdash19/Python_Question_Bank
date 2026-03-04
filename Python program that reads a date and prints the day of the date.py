# Write a Python program that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year.
# Input:
# Two integers m and d separated by a single space in a line, m, d represent the month and the day.
# Input month and date (separated by a single space):
# 5 15
# Name of the date: Sunday

m,d=map(int,input().split())
days=["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]
months=[31,29,31,30,31,30,31,31,30,31,30,31]
total=d-1
for i in range(m-1):
    total+=months[i]
print(days[total%7])