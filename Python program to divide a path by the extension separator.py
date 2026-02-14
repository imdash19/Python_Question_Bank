# Write a Python program to divide a path by the extension separator.

import os

def divide_path_by_extension():
    path = input("Enter the file path: ").strip()

    if not path:
        print("Invalid input! Please enter a valid file path.")
        return

    filename = os.path.basename(path)

    name, extension = os.path.splitext(filename)

    print("=" * 50)
    print(f"Full File Name : {filename}")
    print(f"File Name      : {name}")
    print(f"Extension      : {extension}")

if __name__ == "__main__":
    divide_path_by_extension()