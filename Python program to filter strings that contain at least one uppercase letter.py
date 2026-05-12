# Write a program to filter strings that contain at least one uppercase letter.
# The program should accept comma-separated strings from the user.
# Each string must be checked for uppercase letters.
# Python’s built-in filter() function must be used.
# The output should contain only strings with at least one uppercase letter.

strings = input("Enter comma-separated strings: ").split(",")

result = list(filter(lambda s: any(ch.isupper() for ch in s), strings))

print(result)
