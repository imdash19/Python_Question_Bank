# Write a Python program to convert an integer to binary that keeps leading zeros.

def convert_to_binary_with_leading_zeros():
    try:
        x = int(input("Enter an integer: "))
        width = int(input("Enter total number of bits: "))
        binary_value = format(x, f'0{width}b')

        print("=" * 40)
        print(f"Binary value: {binary_value}")

    except ValueError:
        print("Invalid input! Please enter valid integers.")

convert_to_binary_with_leading_zeros()