# Write a Python program to calculate the least common multiple (LCM) of all numbers in a list.
# The program should ask the user to enter a list of numbers, separated by spaces.
# Each number in the list should be considered for the calculation.
# Use Python’s math.gcd() function to help calculate the LCM of two numbers.
# Use functools.reduce() with a lambda function to compute the LCM successively for all numbers in the list.
# Finally, display the LCM of the entire list as a single integer.

from math import gcd
from functools import reduce

numbers = list(map(int, input("Enter space-separated numbers: ").split()))

lcm = reduce(lambda x, y: (x * y) // gcd(x, y), numbers)

print("LCM of the list:", lcm)
