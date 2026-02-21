# Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system.

import platform
import struct

bit_mode = struct.calcsize("P") * 8
architecture = platform.architecture()[0]

print("Python Bit Mode (using struct):", bit_mode, "bit")
print("Python Architecture (using platform):", architecture)