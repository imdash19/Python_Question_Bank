# Write a Python program to get the third side of a right-angled triangle from two given sides.

import math

print("Right-Angled Triangle - Find the Third Side")
print("1. Find Hypotenuse")
print("2. Find Perpendicular")
print("3. Find Base")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    base = float(input("Enter Base: "))
    perpendicular = float(input("Enter Perpendicular: "))
    hypotenuse = math.sqrt(base**2 + perpendicular**2)
    print("Hypotenuse =", hypotenuse)

elif choice == 2:
    hypotenuse = float(input("Enter Hypotenuse: "))
    base = float(input("Enter Base: "))
    perpendicular = math.sqrt(hypotenuse**2 - base**2)
    print("Perpendicular =", perpendicular)

elif choice == 3:
    hypotenuse = float(input("Enter Hypotenuse: "))
    perpendicular = float(input("Enter Perpendicular: "))
    base = math.sqrt(hypotenuse**2 - perpendicular**2)
    print("Base =", base)

else:
    print("Invalid Choice!")