# Write a Python program to round each float in a given list of numbers up to the next integer and return the running total of the integer squares.
# Input: [2.6, 3.5, 6.7, 2.3, 5.6]
# Output: [9, 25, 74, 83, 119]
# Input: [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
# Output: [91204, 252808, 253337, 183714223444221, 183714327525025, 283714327525025]

import math

lst = [float(val) for val in input('Please enter your values separated with space: ').split()]
olst = []

for val in lst:
    if olst:
        temp = olst[-1] + math.ceil(val) ** 2
        olst.append(temp)
    else:
        olst.append(math.ceil(val) ** 2)

print(olst)