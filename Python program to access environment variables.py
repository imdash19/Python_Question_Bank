# Write a Python program to access environment variables.

import os

var_name = input("Enter environment variable name: ")
value = os.environ.get(var_name)

if value is None:
    print("Environment variable not found.")
else:
    print(f"{var_name} = {value}")