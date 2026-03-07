# Write a Python program to find the number of combinations that satisfy p + q + r + s = n where n is a given number <= 4000 and p, q, r, s are between 0 to 1000.
# Input a positive integer: (ctrl+d to exit)
# 252
# Number of combinations of a, b, c, d: 2731135

import sys

try:
    while True:
        n = int(input())
        count = 0

        for p in range(1001):
            for q in range(1001):
                for r in range(1001):
                    s = n - (p + q + r)
                    if 0 <= s <= 1000:
                        count += 1

        print("Number of combinations of a, b, c, d:", count)

except EOFError:
    pass