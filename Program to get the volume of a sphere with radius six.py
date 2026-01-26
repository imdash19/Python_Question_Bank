# Write a Python program to get the volume of a sphere with radius six.

import math

def calculate_volume(r):
    v = (4 / 3) * math.pi * r**3
    return v

r = float(input("Please enter the radius of the sphere: "))
print("=" * 60)

if r > 0:
    volume = calculate_volume(r)
    print("Volume of the sphere:", volume)
else:
    print("Please enter a positive radius...")