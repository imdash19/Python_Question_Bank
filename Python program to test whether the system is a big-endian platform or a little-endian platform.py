# Write a Python program to test whether the system is a big-endian platform or a little-endian platform.

import sys

def check_endianness():
    if sys.byteorder == "little":
        print("The system is Little-endian.")
    else:
        print("The system is Big-endian.")

check_endianness()