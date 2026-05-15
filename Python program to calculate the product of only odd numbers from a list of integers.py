# Write a Python program to calculate the product of only odd numbers from a list of integers.
# The program should accept space-separated integers from the user.
# From the given list, only odd numbers should be selected.
# Use Python’s filter() function to select odd numbers.
# Use Python’s reduce() function to multiply all selected odd numbers.
# The final output should be a single integer, representing the product of odd numbers.

from functools import reduce

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

product = reduce(lambda x, y: x * y, odd_numbers)

print("Product of odd numbers:", product)
