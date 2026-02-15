# Write a Python program to compute the product of a list of integers (without using a for loop).

from functools import reduce
import operator

def product_of_list():
    try:
        numbers = [int(x) for x in input(
            "Enter integers separated by space: "
        ).split()]

        if not numbers:
            print("The list is empty.")
            return

        product = reduce(operator.mul, numbers)

        print("Product of the list:", product)

    except ValueError:
        print("Error: Please enter only integers.")

product_of_list()