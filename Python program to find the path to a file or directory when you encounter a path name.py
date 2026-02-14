# Write a Python program to find the path to a file or directory when you encounter a path name.

import os

def find_path():
    path = input("Enter the file or directory path: ").strip()

    if not path:
        print("Invalid input!")
        return

    if os.path.exists(path):
        absolute_path = os.path.abspath(path)

        print("=" * 60)
        print(f"Absolute Path : {absolute_path}")

        if os.path.isfile(path):
            print("Type          : File")
        elif os.path.isdir(path):
            print("Type          : Directory")

        print("=" * 60)
    else:
        print("The given path does not exist!")

if __name__ == "__main__":
    find_path()