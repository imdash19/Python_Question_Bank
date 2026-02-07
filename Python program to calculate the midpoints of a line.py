# Write a Python program to calculate the midpoint of a line

def calculate_midpoint():
    x1 = float(input("Enter x1 coordinate: "))
    y1 = float(input("Enter y1 coordinate: "))
    x2 = float(input("Enter x2 coordinate: "))
    y2 = float(input("Enter y2 coordinate: "))

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    print(f"\nMidpoint of the line is: ({midpoint_x}, {midpoint_y})")

calculate_midpoint()