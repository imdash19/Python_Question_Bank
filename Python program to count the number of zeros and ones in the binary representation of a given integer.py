# Write a Python program to count the number of zeros and ones in the binary representation of a given integer.
# Original number: 12
# Number of ones and zeros in the binary representation of the said number: Number of zeros: 2, Number of ones: 2
# Original number: 1234
# Number of ones and zeros in the binary representation of the said number: Number of zeros: 6, Number of ones: 5

n = int(input())
b = bin(n)[2:]
zeros = b.count('0')
ones = b.count('1')
print("Number of zeros:", zeros, ", Number of ones:", ones)