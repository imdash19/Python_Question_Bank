# Write a Python program that will accept the base and height of a triangle and compute its area.

def triangle_area(b, h):
    return ((1/2) * b * h)

b= float(input('Please enter a base: '))
h= float(input('Please enter a height: '))
print(triangle_area(b, h))