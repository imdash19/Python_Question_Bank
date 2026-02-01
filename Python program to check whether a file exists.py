# Write a Python program to check whether a file exists

import os

file_name = input("Enter file name (with extension): ")

if os.path.isfile(file_name):
    print("File exists.")
else:
    print("File does not exist.")