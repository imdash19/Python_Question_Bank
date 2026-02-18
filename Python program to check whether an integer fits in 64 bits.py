# Write a Python program to check whether an integer fits in 64 bits.

def check_64_bit_integer():
    try:
        num = int(input("Enter an integer: "))

        min_val = -2**63
        max_val = 2**63 - 1

        print("=" * 50)

        if min_val <= num <= max_val:
            print("The number fits in a 64-bit signed integer.")
        else:
            print("The number does NOT fit in a 64-bit signed integer.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

check_64_bit_integer()