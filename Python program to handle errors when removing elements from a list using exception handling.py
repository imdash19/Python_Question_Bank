# Write a Python program to handle errors when removing elements from a list using exception handling.
# Here's what you need to do:

# Create a list named numbers with the following values: 10, 20, 30, 40, and 50.
# Take a number as input from the user that they want to remove from the list.
# Use a try block to attempt removing that number from the list using the remove() method.
# If the number exists in the list, remove it and display "Number removed successfully".
# Use an except block to catch the ValueError exception that occurs if the number is not found in the list.
# If the number doesn't exist in the list, display "Error: Number not found in the list".
# The program should not crash even if the number is not present in the list.

# Input Format:

# Single line contains an integer that needs to be removed from the list.

# Output Format:

# If number exists: Display "Number removed successfully".
# If number doesn't exist: Display "Error: Number not found in the list".

try:
    lst= [10, 20, 30, 40, 50]
    n= int(input())

    if n not in lst:
        raise ValueError

except ValueError:
    print('Error: Number not found in the list')

else:
    print('Number removed successfully')
