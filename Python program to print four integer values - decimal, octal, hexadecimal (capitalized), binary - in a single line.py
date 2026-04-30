# Write a Python program to print four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line.
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001

n = int(input("Input an integer: "))

decimal = n
octal = oct(n)[2:]
hexa = hex(n)[2:].upper()
binary = bin(n)[2:]

print("Decimal Octal Hexadecimal Binary")
print(decimal, octal, hexa, binary)