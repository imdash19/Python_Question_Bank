# Write a Python program to find the location of Python module sources.

import importlib

module_name = input("Enter module name: ")

try:
    module = importlib.import_module(module_name)

    if hasattr(module, "__file__") and module.__file__:
        print("Module source location:", module.__file__)
    else:
        print("Built-in module (no source file available).")

except ModuleNotFoundError:
    print("Module not found.")