# Write a Python program to find the highest and lowest number from a given string of space-separated integers.
# Original string: 1 4 5 77 9 0
# Highest and lowest number of the said string: (77, 0)
# Original string: -1 -4 -5 -77 -9 0
# Highest and lowest number of the said string: (0, -77)
# Original string: 0 0
# Highest and lowest number of the said string: (0, 0)

s = input()
nums = list(map(int, s.split()))
print((max(nums), min(nums)))