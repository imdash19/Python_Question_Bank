# Write a Python program to get the details of the math module.

import math

def math_module_details():
    print("Module Name:", math.__name__)
    print("Module File:", math.__file__)
    print("\nModule Documentation:\n")
    print(math.__doc__)

    print("\nAvailable Functions and Constants:\n")
    for item in dir(math):
        print(item)

math_module_details()