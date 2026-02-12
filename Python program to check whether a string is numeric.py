# Write a Python program to check whether a string is numeric.

def check_numeric():
    string = input("Enter a string: ")

    try:
        float(string)  # Try converting to number
        print("It is a numeric.")
    except ValueError:
        print("It is a non-numeric.")

check_numeric()