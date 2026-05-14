# Write a Python program to calculate the total number of characters in a list of strings.
# The program should ask the user to enter a list of strings, separated by commas.
# Each string in the list should be counted for its length.
# Use Python’s functools.reduce() function to sum the lengths of all strings.
# Finally, display the total number of characters as a single integer.

from functools import reduce

strings = input("Enter strings separated by commas: ").split(",")

total_characters = reduce(lambda total, s: total + len(s.strip()), strings, 0)

print("Total number of characters:", total_characters)
