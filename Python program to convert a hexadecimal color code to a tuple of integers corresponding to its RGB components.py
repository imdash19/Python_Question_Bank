# Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.      
# Sample Output:
# (255, 165, 1)
# (255, 255, 255)
# (0, 0, 0)
# (255, 0, 0)
# (0, 0, 128)
# (192, 192, 192)

hex_color = input().strip()

if hex_color.startswith('#'):
    hex_color = hex_color[1:]

r = int(hex_color[0:2], 16)
g = int(hex_color[2:4], 16)
b = int(hex_color[4:6], 16)

print((r, g, b))