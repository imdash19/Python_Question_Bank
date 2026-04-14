# Write a Python program to find four positive even integers whose sum is a given integer.
# Input: n = 100
# Output: [94, 2, 2, 2]
# Input: n = 1000
# Output: [994, 2, 2, 2]
# Input: n = 10000
# Output: [9994, 2, 2, 2]
# Input: n = 1234567890
# Output: [1234567884, 2, 2, 2]

n = int(input())

if n % 2 != 0 or n < 8:
    print("Not possible")
else:
    print([n - 6, 2, 2, 2])