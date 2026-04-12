# Write a Python program to find an integer (n >= 0) with the given number of even and odd digits.
# Input: Number of even digits: 2 ,Number of odd digits: 3
# Output: 22333
# Input: Number of even digits: 4 ,Number of odd digits: 7
# Output: 22223333333

e = int(input())
o = int(input())

print('2'*e + '3'*o)