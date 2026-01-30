# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

a= int(input('Please enter your first value: '))
b= int(input('Please enter your second value: '))
c= int(input('Please enter your third value: '))

print(0) if a == b else print(0) if b == c else print(0) if a == c else print(a+b+c)