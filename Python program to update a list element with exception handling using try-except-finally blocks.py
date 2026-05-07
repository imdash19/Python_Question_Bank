# Write a Python program to update a list element with exception handling using try-except-finally blocks.Here's what you need to do:
# Create a predefined list named items with four values: "apple", "banana", "cherry", and "date".
# Take a value as input from the user that will replace an existing item in the list.
# Take an index position as input from the user where the new value should be placed.
# Use a try block to attempt updating the list at the given index with the new value.
# If the index is out of range, catch the IndexError exception and display an error message.
# Use a finally block that will execute regardless of success or failure, printing "Update attempted" every time.
# If the update is successful, print the updated list after the finally block executes.
# The finally block always runs, whether an exception occurs or not.
# Input Format:
# First line contains the new value as a string.
# Second line contains the index position as an integer.
# Output Format:
# Always print "Update attempted" from the finally block.
# If successful: Print the updated list.
# If index out of range: Print "Error: Index out of range".

items = ["apple", "banana", "cherry", "date"]

value = input()
index = int(input())

try:
    items[index] = value

except IndexError:
    print("Error: Index out of range")

finally:
    print("Update attempted")

if 0 <= index < len(items):
    print(items)
