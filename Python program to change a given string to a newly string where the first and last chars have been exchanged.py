# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

s= input('Please enter a string: ')
print(s[-1]+s[1:-1]+s[0])