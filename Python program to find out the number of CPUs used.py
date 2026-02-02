# Write a Python program to find out the number of CPUs used.

import os
import multiprocessing

def cpu_info():
    print("Number of CPUs (os.cpu_count):", os.cpu_count())
    print("Number of CPUs (multiprocessing):", multiprocessing.cpu_count())

cpu_info()