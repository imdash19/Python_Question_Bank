# Write a Python program to find common divisors between two numbers in a given pair.

def common_divisors():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    divisors = []

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)

    print("Common divisors:", *divisors)

common_divisors()