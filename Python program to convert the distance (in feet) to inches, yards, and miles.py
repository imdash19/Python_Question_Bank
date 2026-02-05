# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

def convert_distance():
    feet = float(input("Enter distance in feet: "))

    inches = feet * 12
    yards = feet / 3
    miles = feet / 5280

    print("\nConverted distances:")
    print("Inches =", inches)
    print("Yards  =", yards)
    print("Miles  =", miles)

convert_distance()