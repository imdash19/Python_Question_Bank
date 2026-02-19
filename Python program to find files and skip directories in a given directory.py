# Write a Python program to find files and skip directories in a given directory.

from pathlib import Path
def list_only_files():
    path = Path(input("Enter directory path: "))
    if not path.exists():
        print("Directory does not exist.")
        return

    print("\nFiles in the directory:")
    print("=" * 40)

    for item in path.iterdir():
        if item.is_file():
            print(item.name)
list_only_files()