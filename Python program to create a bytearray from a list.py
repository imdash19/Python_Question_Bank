# Write a Python program to create a bytearray from a list.

def create_bytearray():
    try:
        values = list(map(int, input("Enter numbers (0-255) separated by space: ").split()))

        for num in values:
            if num < 0 or num > 255:
                raise ValueError("All numbers must be between 0 and 255.")

        b_array = bytearray(values)

        print("\nOriginal List:", values)
        print("Bytearray:", b_array)
        print("Type:", type(b_array))

    except ValueError as e:
        print("Error:", e)

create_bytearray()