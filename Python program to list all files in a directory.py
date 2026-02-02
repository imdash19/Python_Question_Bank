# Write a Python program to list all files in a directory.

import os

def list_files():
    directory = input("Enter directory path: ")

    try:
        files = [
            f for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]

        print("\nFiles in directory:")
        for file in files:
            print(file)

    except FileNotFoundError:
        print("Directory not found!")
    except PermissionError:
        print("Permission denied!")

list_files()