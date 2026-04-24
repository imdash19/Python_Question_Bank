# Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

s = input("Enter a string: ")
s = s.replace(',', '#').replace('.', ',').replace('#', '.')
print(s)