# Write a Python program to get the copyright information and write Copyright information in Python code.

def get_copyright_info():
    print("Python Copyright Information")
    print("-" * 40)
    print(copyright)

get_copyright_info()

from datetime import datetime

def show_my_copyright():
    year = datetime.now().year
    print(f"© {year} Bibhuti Bhusan Dash. All rights reserved.")

show_my_copyright()