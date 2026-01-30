# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

a= int(input('Please enter first value: '))
b= int(input('Please enter second value: '))

print(20) if a+b in range(15, 21) else print(a+b)