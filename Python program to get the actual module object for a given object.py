# Write a Python program to get the actual module object for a given object.

import importlib

def get_module_object():
    module_name = input("Enter module name (e.g., math, sys): ")
    object_name = input("Enter object name (e.g., sqrt, path): ")

    try:
        module = importlib.import_module(module_name)
        obj = getattr(module, object_name)
        actual_module = importlib.import_module(obj.__module__)

        print("\nObject:", obj)
        print("Belongs to module:", obj.__module__)
        print("Actual module object:", actual_module)

    except ModuleNotFoundError:
        print("Module not found!")
    except AttributeError:
        print("Object not found in the given module!")

get_module_object()