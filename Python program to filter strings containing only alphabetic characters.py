# Write a program to filter strings containing only alphabetic characters.
# The program should accept comma-separated strings from the user.
# Each string is checked using isalpha().
# Python’s filter() function must be used.
# The output should contain only strings with alphabets (no digits, spaces, or special characters).

strings = input("Enter comma-separated strings: ").split(",")

result = list(filter(lambda x: x.isalpha(), strings))

print(result)
