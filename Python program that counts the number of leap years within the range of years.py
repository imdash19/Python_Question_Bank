# Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.
# Sample Data:
# ("1981-1991") -> 2
# ("2000-2020") -> 6

year_range = input()

start, end = map(int, year_range.split("-"))

count = 0

for year in range(start, end + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        count += 1

print(count)