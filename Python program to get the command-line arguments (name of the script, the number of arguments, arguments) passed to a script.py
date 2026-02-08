# Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.

import sys

def command_line_arguments():
    script_name = sys.argv[0]
    arguments = sys.argv[1:]
    num_args = len(arguments)

    print("Script name:", script_name)
    print("Number of arguments:", num_args)
    print("Arguments passed:")

    if num_args == 0:
        print("No arguments passed.")
    else:
        for i, arg in enumerate(arguments, start=1):
            print(f"Argument {i}: {arg}")

command_line_arguments()