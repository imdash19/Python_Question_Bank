# Write a Python program to remove the nth index character from a nonempty string.

s= input('Please enter a string: ')
n= int(input('Enter the index to remove the nth character from the string: '))
print(s[:n]+s[n+1:])