# Write a Python program to determine the largest and smallest integers and floats.

import sys
def find_limits():
    print("Choose data type:")
    print("1. Integer")
    print("2. Float")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nInteger Information:")
        print("Minimum practical integer value:", -sys.maxsize - 1)
        print("Maximum practical integer value:", sys.maxsize)
        print("Note: Python int has unlimited precision (only limited by memory).")

    elif choice == "2":
        print("\nFloat Information:")
        print("Minimum positive float:", sys.float_info.min)
        print("Maximum float:", sys.float_info.max)
        print("Smallest negative float:", -sys.float_info.max)

    else:
        print("Invalid choice!")

find_limits()