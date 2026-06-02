# Reads a binary number as input (string of 0s and 1s) and converts it to its decimal (integer) equivalent. The program validates that the input contains only binary digits.

binary = input()

if all(bit in "01" for bit in binary):
    print(int(binary, 2))
else:
    print("Invalid Binary Number")
