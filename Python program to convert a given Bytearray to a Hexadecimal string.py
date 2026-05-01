# Write a Python program to convert a given Bytearray to a Hexadecimal string.
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d

arr = list(map(int, input().split()))
b = bytearray(arr)
print(b.hex())