# Write a Python program to list the special variables used in the language.

def list_special_variables():
    print("Special variables in the current global scope:\n")

    special_vars = [var for var in globals() if var.startswith('__') and var.endswith('__')]

    for var in special_vars:
        print(var)

list_special_variables()