# Write a Python program to print the following integers with '*' to the right of the specified width.

num = int(input())
width = int(input())

print(f"{num:*<{width}}")