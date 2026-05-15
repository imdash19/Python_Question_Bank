# Write a program to find the GCD of two numbers using recursion.
# The program should repeatedly apply Euclidean algorithm.
# If the second number becomes zero, the first number is the GCD.
# The function should call itself until base condition is reached.

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)

print("GCD:", result)
