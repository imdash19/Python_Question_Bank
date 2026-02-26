# Write a Python program to find the median among three given numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

numbers = [a, b, c]
numbers.sort()

print("The median is:", numbers[1])