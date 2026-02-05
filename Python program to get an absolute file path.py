# Write a Python program to get an absolute file path.

import os

def get_absolute_path():
    file_path = input("Enter file path (relative or absolute): ")
    absolute_path = os.path.abspath(file_path)
    print("Absolute file path:", absolute_path)

get_absolute_path()