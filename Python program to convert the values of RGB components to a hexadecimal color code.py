# Write a Python program to convert the values of RGB components to a hexadecimal color code.
# Sample Output:
# FFA501
# FFFFFF
# 000000
# 000080
# C0C0C0

r = int(input())
g = int(input())
b = int(input())

if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
    print("Error: RGB values must be between 0 and 255")
else:
    print("{:02X}{:02X}{:02X}".format(r, g, b))