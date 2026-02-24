# Write a Python program to get a list of locally installed Python modules.

import pkgutil

def list_installed_modules():
    print("\nFetching installed Python modules...\n")
    print("=" * 60)

    modules = sorted([module.name for module in pkgutil.iter_modules()])

    for module in modules:
        print(module)

    print("\n" + "=" * 60)
    print(f"Total Installed Modules: {len(modules)}")

list_installed_modules()