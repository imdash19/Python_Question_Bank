# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

result = (a == b) or (a + b == 5) or (abs(a - b) == 5)
print(result)