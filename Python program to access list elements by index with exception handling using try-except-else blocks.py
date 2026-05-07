# Write a Python program to access list elements by index with exception handling using try-except-else blocks.Here's what you need to do:
# Create a list named items with the following values: "apple", "banana", "cherry", "date", and "elderberry".
# Take an index position as input from the user.
# Use a try block to convert the input to an integer and access the element at that index position from the list.
# If the index is out of range (either negative beyond the list size or greater than the last valid index), catch the IndexError exception and display an error message.
# Use an else block that executes only when the element is successfully accessed without any exception.
# Inside the else block, display the item that was found at the given index.
# The program should handle both valid and invalid indices without crashing.
# Input Format:
# Single line contains an integer representing the index position.
# Output Format:
# If valid index: Display "Item at index [index]: [item_name]".
# If invalid index: Display "Error: Index out of range".

try:
    lst= ["apple", "banana", "cherry", "date", "elderberry"]
    n= int(input())

    res= lst[n]

except IndexError:
    print('Error: Index out of range')

except ValueError:
    print('Error: Invalid input. Please enter a valid number')

else:
    print(f'Item at index {n}: {res}')
