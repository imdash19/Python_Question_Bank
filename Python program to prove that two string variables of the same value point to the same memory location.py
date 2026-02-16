# Write a Python program to prove that two string variables of the same value point to the same memory location.

def check_string_memory():
    string1 = input("Enter a string value: ")
    string2 = string1   # Assign same value

    print("\nString 1:", string1)
    print("String 2:", string2)

    print("\nMemory location of string1:", id(string1))
    print("Memory location of string2:", id(string2))

    if string1 is string2:
        print("\n✅ Both variables point to the same memory location.")
    else:
        print("\n❌ Variables point to different memory locations.")

check_string_memory()