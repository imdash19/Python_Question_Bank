# A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees.
# Write a Python program that compute the area of the polygon. The vertices have the names vertex 1, vertex 2, vertex 3, ... vertex n according to the order of edge connections
# Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and consecutive letters are not more than 9 letters.
# Input:
# Input number of sides: 5
# Side: 1
# Input the Coordinate:
# Input Coordinate x: 1
# Input Coordinate y: 0
# Side: 2
# Input the Coordinate:
# Input Coordinate x: 0
# Input Coordinate y: 0
# Side: 3
# Input the Coordinate:
# Input Coordinate x: 1
# Input Coordinate y: 1
# Side: 4
# Input the Coordinate:
# Input Coordinate x: 2
# Input Coordinate y: 0
# Side: 5
# Input the Coordinate:
# Input Coordinate x: -1
# Input Coordinate y: 1
# Area of the Polygon: 0.5

n = int(input("Input number of sides: "))
x = []
y = []

for i in range(n):
    print("Side:", i+1)
    print("Input the Coordinate:")
    xi = float(input("Input Coordinate x: "))
    yi = float(input("Input Coordinate y: "))
    x.append(xi)
    y.append(yi)

area = 0
for i in range(n):
    j = (i + 1) % n
    area += x[i] * y[j] - y[i] * x[j]

area = abs(area) / 2
print("Area of the Polygon:", area)