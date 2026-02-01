# Write a Python program to check whether Python is running in 32-bit or 64-bit mode

import struct

if struct.calcsize("P") * 8 == 64:
    print("Python is running in 64-bit mode")
else:
    print("Python is running in 32-bit mode")