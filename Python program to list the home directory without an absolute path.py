# Write a Python program to list the home directory without an absolute path.

import os


def list_home_directory():
    try:
        home_dir = os.path.expanduser("~")
        print(f"\nHome Directory: {home_dir}")
        print("=" * 50)
        items = os.listdir(home_dir)
        if items:
            for item in items:
                print(item)
        else:
            print("Home directory is empty.")
    except Exception as e:
        print("Error:", e)

list_home_directory()