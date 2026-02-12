# Write a Python program to print the current call stack.

import traceback

def function_three():
    print("Current Call Stack:\n")
    traceback.print_stack()

def function_two():
    function_three()

def function_one():
    function_two()

function_one()