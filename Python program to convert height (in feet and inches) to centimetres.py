# Write a Python program to convert height (in feet and inches) to centimetres.

def height_to_centimeters():
    feet = int(input("Enter height (feet): "))
    inches = int(input("Enter remaining height (inches): "))

    if feet < 0 or inches < 0:
        print("Height values must be non-negative.")
        return

    total_cm = (feet * 30.48) + (inches * 2.54)
    print(f"Height in centimeters: {total_cm:.2f} cm")

height_to_centimeters()