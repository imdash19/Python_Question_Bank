# Write a Python program to add leading zeroes to a string.

def add_leading_zeroes():
    text = input("Enter a string or number: ")
    width = int(input("Enter total desired length: "))
    print("=" * 50)
    result = text.zfill(width)
    print("Result after adding leading zeroes:", result)

add_leading_zeroes()