# Write a Python program to calculate the greatest common divisor (GCD) of all numbers in a list.
# The program should ask the user to enter a list of numbers, separated by spaces.
# Each number in the list should be considered for the calculation.
# Use Python’s math.gcd() function to find the GCD of two numbers.
# Use functools.reduce() to apply the GCD function successively to all numbers in the list.
# Finally, display the GCD of the entire list as a single integer.

from math import gcd
from functools import reduce

numbers = list(map(int, input("Enter space-separated numbers: ").split()))

result = reduce(gcd, numbers)

print("GCD of the list:", result)
