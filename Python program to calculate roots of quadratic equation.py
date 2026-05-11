# Write a program that takes three numbers a, b, and c as input in a single line separated by spaces, representing the coefficients of a quadratic equation ax² + bx + c = 0. Calculate and print the two roots of the equation. The input will be three numbers separated by spaces, and the output should display both roots, which can be real or complex numbers.

import math
import cmath

a, b, c = map(float, input().split())

d = b**2 - 4*a*c

root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print(root1)
print(root2)
