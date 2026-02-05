# Write a Python program to calculate the hypotenuse of a right-angled triangle.

import math

def calculate_hypotenuse():
    a = float(input("Enter one side length: "))
    b = float(input("Enter another side length: "))

    if a <= 0 or b <= 0:
        return "Side lengths must be positive numbers."

    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

result = calculate_hypotenuse()
print("Hypotenuse =", result)