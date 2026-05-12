# Write a program to filter strings ending with a specific character.
# The program should accept:
# Comma-separated strings from the user
# A single character to check
# Each string is checked for its last character.
# Python’s built-in filter() function must be used.
# The output should contain only strings ending with the given character.

strings = input("Enter comma-separated strings: ").split(",")
char = input("Enter a character: ")

result = list(filter(lambda x: x.endswith(char), strings))

print("Strings ending with", char, "are:")
print(result)
