# Write a Python program to convert the bytes in a given string to a list of integers.

def bytes_to_integer_list():
    print("=" * 60)
    print("Convert Bytes of a String to List of Integers")
    print("=" * 60)

    user_string = input("Enter a string: ")
    byte_data = user_string.encode()
    integer_list = list(byte_data)

    print("\nOriginal String :", user_string)
    print("Byte Representation :", byte_data)
    print("List of Integers :", integer_list)
    print("=" * 60)

bytes_to_integer_list()