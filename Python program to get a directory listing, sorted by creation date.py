# Write a Python program to get a directory listing, sorted by creation date.

import os
from datetime import datetime

def directory_listing_by_creation_date():
    directory = input("Enter the directory path: ").strip()

    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return

    files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]

    files.sort(key=lambda x: os.path.getctime(x))

    print("\nDirectory listing (oldest → newest):\n")
    for file in files:
        created_time = datetime.fromtimestamp(os.path.getctime(file))
        print(f"{os.path.basename(file)}  |  Created on: {created_time}")