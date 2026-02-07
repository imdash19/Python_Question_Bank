# Write a Python program to sort files by date.

import os

def sort_files_by_date():
    directory = input("Enter the directory path: ").strip()

    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return

    files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]

    files.sort(key=lambda x: os.path.getmtime(x))

    print("\nFiles sorted by date (oldest → newest):\n")
    for file in files:
        modified_time = os.path.getmtime(file)
        print(f"{os.path.basename(file)}")

sort_files_by_date()