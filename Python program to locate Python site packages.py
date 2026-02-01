# Write a Python program to locate Python site-packages

import site

site_packages = site.getsitepackages()

print("Python site-packages locations:")
for path in site_packages:
    print(path)