# Write a Python program to determine if a variable is defined or not.

def check_variable_defined():
    var_name = input("Enter the variable name to check: ")

    if var_name in globals() or var_name in locals():
        print(f"Variable '{var_name}' is defined.")
    else:
        print(f"Variable '{var_name}' is NOT defined.")

x = 100
check_variable_defined()