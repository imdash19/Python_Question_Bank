# Write a program to filter strings that contain at least one whitespace.
# The program should accept comma-separated strings from the user.
# Each string is checked for the presence of a space character.
# Python’s filter() function must be used.
# The output should contain only strings that include at least one space.

strings = input("Enter comma-separated strings: ").split(",")

result = list(filter(lambda x: " " in x, strings))

print(result)
