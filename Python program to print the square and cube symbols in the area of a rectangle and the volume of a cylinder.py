# Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3

area = float(input("Enter area of rectangle: "))
volume = float(input("Enter volume of cylinder: "))

print("The area of the rectangle is", format(area, ".2f"), "cm\u00b2")
print("The volume of the cylinder is", format(volume, ".3f"), "cm\u00b3")