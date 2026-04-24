# Write a Python program to split a string on the last occurrence of the delimiter.

s = input("Enter the string: ")
delimiter = input("Enter the delimiter: ")
parts = s.rsplit(delimiter, 1)
print(parts)