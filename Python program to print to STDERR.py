# Write a Python program to print to STDERR

import sys

message = input("Enter an error message: ")
print(message, file=sys.stderr)