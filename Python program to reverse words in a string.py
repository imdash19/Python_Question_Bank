# Write a Python program to reverse words in a string.

lst= list(input('Please enter your string: '))
for val in lst:
    print(val[::-1], end= ' ')