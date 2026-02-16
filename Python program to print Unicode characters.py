# Write a Python program to print Unicode characters.

def print_unicode_characters():
    try:
        start = int(input("Enter starting Unicode value (e.g., 65): "))
        end = int(input("Enter ending Unicode value (e.g., 75): "))

        print("\nUnicode Characters:\n")
        for code in range(start, end + 1):
            print(f"Unicode {code} : {chr(code)}")

    except ValueError:
        print("Error: Please enter valid integer values.")

print_unicode_characters()