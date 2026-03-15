# Write a Python program to check whether two given lines are parallel or not.
# Note: Parallel lines are two or more lines that never intersect. Parallel Lines are like railroad tracks that never intersect.
# The General Form of the equation of a straight line is: ax + by = c
# The said straight line is represented in a list as [a, b, c]
# Example of two parallel lines:
# x + 4y = 10 and x + 4y = 14
# Sample Input:
# ([2,3,4], [2,3,8])
# ([2,3,4], [4,-3,8])
# Sample Output:
# True
# False

l1 = eval(input())
l2 = eval(input())

a1, b1, c1 = l1
a2, b2, c2 = l2

if a1*b2 == a2*b1:
    print(True)
else:
    print(False)