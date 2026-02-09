# Write a Python program to get the current value of the recursion limit.

import sys

def get_recursion_limit():
    limit = sys.getrecursionlimit()
    print(f"Current recursion limit is: {limit}")

get_recursion_limit()