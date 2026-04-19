# Write a Python program to check whether a string starts with specified characters.

s = input()
prefix = input()

if s.startswith(prefix):
    print("The string starts with the specified characters.")
else:
    print("The string does not start with the specified characters.")