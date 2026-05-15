# Write a Python program to calculate the minimum difference between consecutive numbers in a list.
# The program should ask the user to enter a list of integers, separated by spaces.
# Calculate the absolute difference between each pair of consecutive numbers.
# Use Python’s functools.reduce() function to find the smallest difference successively.
# Finally, display the minimum difference as a single integer.

from functools import reduce

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

differences = [abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1)]

minimum_difference = reduce(lambda x, y: x if x < y else y, differences)

print("Minimum difference:", minimum_difference)
