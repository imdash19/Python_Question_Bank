# Write a Python program to calculate the product of all even numbers in a list.
# The program should ask the user to enter a list of integers, separated by spaces.
# Use Python’s filter() function to select only even numbers.
# Use functools.reduce() to multiply the filtered numbers successively.
# Finally, display the product as a single integer.

from functools import reduce

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

product = reduce(lambda x, y: x * y, even_numbers, 1)

print("Product of all even numbers:", product)
