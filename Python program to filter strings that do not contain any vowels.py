# Write a program to filter strings that do not contain any vowels.
# The program should accept comma-separated strings from the user.
# Each string must be checked for the presence of vowels (a, e, i, o, u, both uppercase and lowercase).
# Python’s filter() function must be used.
# The output should contain only strings with no vowels.

strings = input("Enter comma-separated strings: ").split(",")

vowels = "aeiouAEIOU"

result = list(filter(lambda s: not any(ch in vowels for ch in s), strings))

print(result)
