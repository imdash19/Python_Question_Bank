# Write a Python program to get OS name, platform, and release information

import platform
import os

print("OS Name        :", os.name)
print("Platform       :", platform.system())
print("OS Release     :", platform.release())