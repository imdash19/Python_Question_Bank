# Reads a large integer and formats it with comma separators for thousands using .format() method. Improves readability of large numbers.

number = int(input())

print("{:,}".format(number))
