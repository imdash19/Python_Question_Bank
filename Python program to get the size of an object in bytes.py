# Write a Python program to get the size of an object in bytes.

import sys

def get_object_size():
    obj = input("Enter any value: ")

    size = sys.getsizeof(obj)

    print(f"Object: {obj}")
    print(f"Size in bytes: {size}")

get_object_size()