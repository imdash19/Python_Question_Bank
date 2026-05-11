# Write a Python program to count the number of set bits (1s) in an integer.
# The program should ask the user to enter an integer.
# Convert the integer to a binary string using Python’s bin() function.
# Use the string method count() to count the number of 1s in the binary representation.
# Display the result clearly.
# Hint:
# The bin() function returns a string like '0b1011'.

# Only the part after '0b' is the actual binary representation.

def count_set_bits(n):
    binary = bin(n)[2:]
    return binary.count('1')

if __name__ == "__main__":
    n = int(input())
    print('Number of set bits: ', count_set_bits(n))
