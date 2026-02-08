# Write a Python program to find the available built-in modules.

import sys

def list_builtin_modules():
    modules = sys.builtin_module_names

    print("Available Built-in Modules")
    print("-" * 40)
    print(f"Total modules: {len(modules)}\n")

    for module in modules:
        print(module)

list_builtin_modules()