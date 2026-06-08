# Reads hour, minute, and second components and formats them as a standardized time string (HH:MM:SS) using .format() method. Ensures consistent time display with leading zeros.

hour = int(input())
minute = int(input())
second = int(input())

print("{:02d}:{:02d}:{:02d}".format(hour, minute, second))