# A Python list contains two positive integers. Write a Python program to check whether the cube root of the first number is equal to the square root of the second number.
# Sample Data:
# ([8, 4]) -> True
# ([64, 16]) -> True
# ([64, 36]) -> False

import math


def check_numbers(lst):
    a, b = lst

    cube_root = a ** (1 / 3)
    square_root = math.sqrt(b)

    print(round(cube_root, 5) == round(square_root, 5))


check_numbers(list(map(int, input().split())))