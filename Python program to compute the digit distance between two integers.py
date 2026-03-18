# Write a Python program to compute the digit distance between two integers.
# The digit distance between two numbers is the absolute value of the difference of those numbers.
# For example, the distance between 3 and -3 on the number line given by the |3 - (-3) | = |3 + 3 | = 6 units
# Digit distance of 123 and 256 is
# Since |1 - 2| + |2 - 5| + |3 - 6| = 1 + 3 + 3 = 7
# Sample Input:
# (123, 256)
# (23, 56)
# (1, 2)
# (24232, 45645)
# Sample Output:
# 7
# 6
# 1
# 11

n1, n2 = input().strip('()').split(',')

n1 = n1.strip()
n2 = n2.strip()

max_len = max(len(n1), len(n2))

n1 = n1.zfill(max_len)
n2 = n2.zfill(max_len)

distance = 0

for d1, d2 in zip(n1, n2):
    distance += abs(int(d1) - int(d2))

print(distance)