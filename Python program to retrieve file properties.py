# Write a Python program to retrieve file properties.

import os
import time

def get_file_properties():
    path = input("Enter the file path: ").strip()

    if not os.path.exists(path):
        print("File does not exist!")
        return

    print("=" * 60)

    print(f"File Name        : {os.path.basename(path)}")
    print(f"Absolute Path    : {os.path.abspath(path)}")
    print(f"File Size        : {os.path.getsize(path)} bytes")
    print(f"Created Time     : {time.ctime(os.path.getctime(path))}")
    print(f"Modified Time    : {time.ctime(os.path.getmtime(path))}")
    print(f"Last Access Time : {time.ctime(os.path.getatime(path))}")

    print("=" * 60)

if __name__ == "__main__":
    get_file_properties()