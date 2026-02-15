# Write a Python program to make file lists from the current directory using a wildcard.

import glob
import os

def list_files_with_wildcard():
    pattern = input("Enter wildcard pattern (example: *.txt, *.py, *.*): ")

    current_dir = os.getcwd()
    print(f"\nCurrent Directory: {current_dir}\n")
    search_pattern = os.path.join(current_dir, pattern)
    files = glob.glob(search_pattern)

    if files:
        print("Matching files:")
        for file in files:
            print(os.path.basename(file))
    else:
        print("No files found matching the pattern.")

list_files_with_wildcard()