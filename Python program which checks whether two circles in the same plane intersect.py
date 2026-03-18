# Write a Python program which checks whether two circles in the same plane (with the same centre (x, y) and radius) intersect. If intersection occurs, return true, otherwise return false.
# Sample Input:
# ([1,2, 4], [1,2, 8])
# ([0,0, 2], [10,10, 5])
# Sample Output:
# True
# False

import math

c1 = list(map(int, input().strip('[]').split(',')))
c2 = list(map(int, input().strip('[]').split(',')))

x1, y1, r1 = c1
x2, y2, r2 = c2

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distance <= r1 + r2:
    print(True)
else:
    print(False)