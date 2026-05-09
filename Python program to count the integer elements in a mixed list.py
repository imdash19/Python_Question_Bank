# Write a Python program to count the integer elements in a mixed list.
# The program should ask the user to enter a space-separated list containing numbers, strings, and floats.
# Use Python’s isinstance() function to check each element.
# Count only integers in the list.
# Display the total count clearly.
# Hint:
# isinstance(element, int) returns True if the element is an integer.
# You may need to convert input strings to numbers when possible.

lst= [int(val) for val in input().split() if val.lstrip('-').isdigit()]
print(len(lst))
