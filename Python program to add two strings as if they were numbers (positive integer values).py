# Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if the numbers are strings.
# Sample Output:
# 42
# Error in input!
# Error in input!

a = input("Enter first string: ")
b = input("Enter second string: ")

if a.isdigit() and b.isdigit():
    result = int(a) + int(b)
    print(result)
else:
    print("Error in input!")