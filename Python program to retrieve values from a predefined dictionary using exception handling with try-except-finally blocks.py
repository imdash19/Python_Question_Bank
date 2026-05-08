# Write a Python program to retrieve values from a predefined dictionary using exception handling with try-except-finally blocks.Here's what you need to do:
# Create a predefined dictionary named data with three key-value pairs: "name" with value "Abhi", "age" with value 22, and "course" with value "Python".
# Take a key name as input from the user that they want to search in the dictionary.
# Use a try block to attempt retrieving the value for the given key from the dictionary.
# If the key exists in the dictionary, store and display its corresponding value.
# If the key does not exist, Python will raise a KeyError exception which you need to catch in the except block.
# Display an appropriate error message when the key is not found in the dictionary.
# Use a finally block that always executes and prints "Access attempted" regardless of whether the key was found or not.
# The finally block ensures that the access attempt is logged every time, similar to how databases track all query attempts.
# The program should handle both existing and non-existing keys without crashing.
# Input Format:
# Single line contains a key name as a string.
# Output Format:
# Always print "Access attempted" from the finally block.
# If key exists: Display the value associated with that key.
# If key doesn't exist: Display "Error: Key not found in dictionary".

try:
    d= {'name': 'Abhi', 'age': 22, 'cource': 'python'}
    k= input()
    print(d[k])

except KeyError:
    print('Error: Key not found in dictionary')

finally:
    print('Access attempted')
