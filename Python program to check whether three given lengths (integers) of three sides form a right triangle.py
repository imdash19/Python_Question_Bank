# Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No".
# Input:
# Integers separated by a single space.
# 1 <= length of the side <= 1,000
# Input three integers (sides of a triangle)
# 8 6 7
# No

a, b, c = map(int, input().split())

sides = sorted([a, b, c])

if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("Yes")
else:
    print("No")