# Write a Python program to convert decimal to hexadecimal.

def decimal_to_hex():
    try:
        numbers = [int(x) for x in input("Enter decimal numbers separated by space: ").split()]

        print("=" * 40)
        print("Hexadecimal values:")

        for num in numbers:
            hex_value = format(num, 'x')
            hex_value = hex_value.zfill(2)

            print(hex_value)

    except ValueError:
        print("Invalid input! Please enter valid integers.")

decimal_to_hex()