# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Dynamic input
num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

gcd = compute_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)