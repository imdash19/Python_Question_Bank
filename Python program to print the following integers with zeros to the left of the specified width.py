# Write a Python program to print the following integers with zeros to the left of the specified width.

num = int(input())
width = int(input())

print(f"{num:0{width}d}")