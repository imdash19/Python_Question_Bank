# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output: r = 1.1
# Area = 3.8013271108436504

import math

def calculate_area(r):
    return math.pi * r**2

r= float(input('Enter the radious of circle: '))
print(f'Area of circle is: {calculate_area(r)}')