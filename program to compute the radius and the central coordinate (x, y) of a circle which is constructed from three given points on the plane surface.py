# Write a program to compute the radius and the central coordinate (x, y) of a circle which is constructed from three given points on the plane surface.
# Input:
# x1, y1, x2, y2, x3, y3 separated by a single space.
# Input three coordinates of the circle:
# 9 3 6 8 3 6
# Radius of the said circle:
# 3.358
# Central coordinate (x, y) of the circle:
# 6.071 4.643

import math

x1, y1, x2, y2, x3, y3 = map(float, input("Input three coordinates of the circle:\n").split())

A = x2 - x1
B = y2 - y1
C = x3 - x1
D = y3 - y1

E = A * (x1 + x2) + B * (y1 + y2)
F = C * (x1 + x3) + D * (y1 + y3)

G = 2 * (A * (y3 - y2) - B * (x3 - x2))

if G == 0:
    print("The points are collinear")
else:
    cx = (D * E - B * F) / G
    cy = (A * F - C * E) / G
    r = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)

    print("Radius of the said circle:")
    print(f"{r:.3f}")
    print("Central coordinate (x, y) of the circle:")
    print(f"{cx:.3f} {cy:.3f}")