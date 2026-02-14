# Write a Python program to get the user environment.

import os

def get_user_environment():
    var_name = input("Enter the environment variable name: ").strip()

    if not var_name:
        print("Invalid input! Please enter a valid environment variable name.")
        return

    value = os.environ.get(var_name)

    if value is None:
        print(f"{var_name} is not set in the environment.")
    else:
        print(f"{var_name} = {value}")

if __name__ == "__main__":
    get_user_environment()