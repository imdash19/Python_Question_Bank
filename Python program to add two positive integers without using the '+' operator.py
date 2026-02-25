# Write a Python program to add two positive integers without using the '+' operator.
# Note: Use bit wise operations to add two numbers.

a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

while b != 0:
    carry = a & b
    a = a ^ b
    b = carry << 1

print("Sum is:", a)