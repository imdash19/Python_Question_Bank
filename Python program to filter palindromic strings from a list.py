# Write a program to filter palindromic strings from a list.
# The program should accept comma-separated strings from the user.
# Each string must be checked by comparing it with its reverse.
# Python’s built-in filter() function must be used.
# The output should contain only palindromic strings.

strings = input("Enter comma-separated strings: ").split(",")

result = list(filter(lambda s: s == s[::-1], strings))

print(result)
