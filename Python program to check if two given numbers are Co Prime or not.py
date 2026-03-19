# Write a Python program to check if two given numbers are Co Prime or not. Return True if two numbers are Co Prime otherwise return false.
# Sample Input:
# (17, 13)
# (17, 21)
# (15, 21)
# (25, 45)
# Sample Output:
# True
# True
# False
# False

import math

def coprime(a, b):
    return math.gcd(a, b) == 1

t = int(input())
for _ in range(t):
    a, b = eval(input())
    print(coprime(a, b))