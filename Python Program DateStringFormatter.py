# Reads year, month, and day components and formats them as a standardized date string (YYYY-MM-DD) using .format() method. Ensures consistent date display formatting.

year = int(input())
month = int(input())
day = int(input())

print("{:04d}-{:02d}-{:02d}".format(year, month, day))