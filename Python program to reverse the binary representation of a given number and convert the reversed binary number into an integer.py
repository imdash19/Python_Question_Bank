# Write a Python program to reverse the binary representation of a given number and convert the reversed binary number into an integer.
# Original number: 13
# Reverse the binary representation of the said integer and convert it into an integer: 11
# Original number: 145
# Reverse the binary representation of the said integer and convert it into an integer: 137
# Original number: 1342
# Reverse the binary representation of the said integer and convert it into an integer: 997

n = int(input())
b = bin(n)[2:]
r = b[::-1]
print(int(r, 2))