# Write a Python program to create a copy of its own source code.

import os


def copy_own_source():
    try:
        source_file = os.path.abspath(__file__)

        print("=" * 50)
        print(f"Current source file: {source_file}")
        print("=" * 50)

        new_file_name = input("Enter the name for the copied file (with .py extension): ").strip()

        if not new_file_name.endswith(".py"):
            print("Invalid file name! Must end with .py")
            return

        with open(source_file, "r") as file:
            content = file.read()

        with open(new_file_name, "w") as new_file:
            new_file.write(content)

        print("=" * 50)
        print(f"Successfully created a copy as '{new_file_name}'")
        print("=" * 50)

    except Exception as e:
        print("Error:", e)


copy_own_source()