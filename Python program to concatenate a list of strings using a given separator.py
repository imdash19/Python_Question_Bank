# Write a Python program to concatenate a list of strings using a given separator.
# The program should accept comma-separated strings from the user.
# The program should also accept a single separator character.
# Use Python’s reduce() function along with a lambda expression to join the strings.
# The final output should be one single concatenated string with the separator placed between each string.

from functools import reduce

strings = input("Enter comma-separated strings: ").split(",")
separator = input("Enter a separator character: ")
result = reduce(lambda x, y: x + separator + y, strings)

print("Concatenated string:", result)
