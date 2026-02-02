# Write a Python program to retrieve the path and name of the file currently being executed.

import os

def get_current_file_info():
    file_path = os.path.abspath(__file__)
    file_name = os.path.basename(__file__)

    print("Full file path :", file_path)
    print("File name      :", file_name)

get_current_file_info()