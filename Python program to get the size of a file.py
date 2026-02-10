# Write a Python program to get the size of a file.

import os

def get_file_size():
    file_path = input("Enter the file path: ")

    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
        print(f"File size: {size} bytes")
    else:
        print("Invalid file path or file does not exist.")

get_file_size()