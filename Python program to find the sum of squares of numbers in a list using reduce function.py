# Write a Python program to find the sum of squares of numbers in a list.
# The program should accept space-separated integers from the user.
# Each number must be squared.
# Use Python’s map() function to calculate the square of each number.
# Use Python’s reduce() function to add all squared values.
# The final output should be one integer, representing the sum of squares.

from functools import reduce

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

squares = list(map(lambda x: x ** 2, numbers))

sum_of_squares = reduce(lambda x, y: x + y, squares)

print("Sum of squares:", sum_of_squares)
