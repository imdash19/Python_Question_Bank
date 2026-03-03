# Write a Python program to test whether two lines PQ and RS are parallel. The four points are P (x1, y1), Q (x2, y2), R (x3, y3), S (x4, y4).
# Input: x1, y1, x2, y2, x3, y3, xp, yp separated by a single space
# Input x1, y1, x2, y2, x3, y3, xp, yp: 2 5 6 4 8 3 9 7
# PQ and RS are not parallel

def check_parallel():
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
        print("PQ and RS are parallel")
    else:
        print("PQ and RS are not parallel")

check_parallel()