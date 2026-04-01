# Write a Python program to find the coordinates of a triangle with given side lengths.
# Input:
# [3, 4, 5]
# Output:
# [[0.0, 0.0], [3, 0.0], [3.0, 4.0]]
# Input:
# [5, 6, 7]
# Output:
# [[0.0, 0.0], [5, 0.0], [3.8, 5.878775382679628]]

import math

sides = list(map(float, input().strip('[]').split(',')))

a, b, c = sides

x1, y1 = 0.0, 0.0
x2, y2 = a, 0.0

x3 = (c*c + a*a - b*b) / (2*a)
y3 = math.sqrt(c*c - x3*x3)

print([[x1, y1], [x2, y2], [x3, y3]])