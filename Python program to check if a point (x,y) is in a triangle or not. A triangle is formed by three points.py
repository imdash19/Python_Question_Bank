# Write a Python program to check if a point (x,y) is in a triangle or not. A triangle is formed by three points.
# Input:
# x1, y1, x2, y2, x3, y3, xp, yp separated by a single space.
# Input three coordinates of the circle:
# 9 3 6 8 3 6
# Radius of the said circle:
# 3.358
# Central coordinate (x, y) of the circle:
# 6.071 4.643

x1, y1, x2, y2, x3, y3, xp, yp = map(float, input("Input x1 y1 x2 y2 x3 y3 xp yp:\n").split())

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

A = area(x1, y1, x2, y2, x3, y3)
A1 = area(xp, yp, x2, y2, x3, y3)
A2 = area(x1, y1, xp, yp, x3, y3)
A3 = area(x1, y1, x2, y2, xp, yp)

if abs(A - (A1 + A2 + A3)) < 1e-6:
    print("The point is inside the triangle")
else:
    print("The point is not inside the triangle")