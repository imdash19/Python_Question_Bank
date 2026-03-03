# There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2).
# Write a Python program to test the followings -
# "C2 is in C1" if C2 is in C1
# "C1 is in C2" if C1 is in C2
# "Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect
# "C1 and C2 do not overlap" if C1 and C2 do not overlap and
# "Circumference of C1 and C2 will touch" if C1 and C2 touch
# Input: Input numbers (real numbers) are separated by a space.
# Input x1, y1, r1, x2, y2, r2: 5 4 2 3 9 2
# C1 and C2 do not overlap
# Input x1, y1, r1, x2, y2, r2: 5 4 3 5 10 3
# Circumference of C1 and C2 will touch
# Input x1, y1, r1, x2, y2, r2: 6 4 3 10 4 2
# Circumference of C1 and C2 intersect
# Input x1, y1, r1, x2, y2, r2: 5 4 3 5 4 2
# C2 is in C1
# Input x1, y1, r1, x2, y2, r2: 5 4 2 5 4 3
# C1 is in C2

import math

def check_circles():
    while True:
        try:
            x1, y1, r1, x2, y2, r2 = map(float, input("Input x1, y1, r1, x2, y2, r2: ").split())
        except:
            break
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if d + r2 < r1:
            print("C2 is in C1")
        elif d + r1 < r2:
            print("C1 is in C2")
        elif d == r1 + r2 or d == abs(r1 - r2):
            print("Circumference of C1 and C2 will touch")
        elif d > r1 + r2:
            print("C1 and C2 do not overlap")
        else:
            print("Circumference of C1 and C2 intersect")

check_circles()