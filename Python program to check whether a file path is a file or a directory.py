# Write a Python program to check whether a file path is a file or a directory.

import os

def check_path():
    path = input("Enter a file or directory path: ")

    if os.path.isfile(path):
        print("The given path is a FILE.")
    elif os.path.isdir(path):
        print("The given path is a DIRECTORY.")
    else:
        print("The given path is NOT valid.")

check_path()