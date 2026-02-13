# Write a Python program to extract the filename from a given path.

import os

def extract_filename():
    path = input("Enter the file path: ")

    filename = os.path.basename(path)
    print("Filename:", filename)

extract_filename()