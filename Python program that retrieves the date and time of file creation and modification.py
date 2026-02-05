# Write a Python program that retrieves the date and time of file creation and modification.

import os
import time

def get_file_dates():
    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    created_time = os.path.getctime(file_path)
    modified_time = os.path.getmtime(file_path)

    print("\nFile Dates:")
    print("Created on   :", time.ctime(created_time))
    print("Modified on  :", time.ctime(modified_time))

get_file_dates()