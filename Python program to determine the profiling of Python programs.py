# Write a Python program to determine the profiling of Python programs.
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.

import cProfile
import pstats

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    num = int(input("Enter a number: "))
    result = factorial(num)
    print("Factorial:", result)

cProfile.run("main()", "profile_stats")

stats = pstats.Stats("profile_stats")
stats.strip_dirs().sort_stats("time").print_stats()