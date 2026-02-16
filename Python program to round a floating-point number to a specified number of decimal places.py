# Write a Python program to round a floating-point number to a specified number of decimal places.

def round_float_number():
    try:
        number = float(input("Enter a floating-point number: "))
        decimals = int(input("Enter number of decimal places: "))
        rounded_value = round(number, decimals)
        print("\nOriginal Number:", number)
        print("Rounded Number:", rounded_value)

    except ValueError:
        print("Error: Please enter valid numeric values.")

round_float_number()