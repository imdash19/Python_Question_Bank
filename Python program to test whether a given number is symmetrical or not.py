# Write a Python program to test whether a given number is symmetrical or not. A number is symmetrical when it is equal to its reverse.
# A number is symmetrical when it is equal of its reverse.
# Sample Input:
# (121)
# (0)
# (122)
# (990099)
# Sample Output:
# True
# True
# False
# True

n=input().strip("()")

print(n==n[::-1])