# Write a Python program to parse a string to float or integer.

def parse_number():
    value = input("Enter a number: ")

    try:
        number = int(value)
        print("Parsed as Integer:", number)
    except ValueError:
        try:
            number = float(value)
            print("Parsed as Float:", number)
        except ValueError:
            print("Invalid number! Cannot parse.")

parse_number()