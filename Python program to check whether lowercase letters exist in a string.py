# Write a Python program to check whether lowercase letters exist in a string.

def check_lowercase():
    text = input("Enter a string: ")

    print("=" * 50)

    has_lowercase = any(char.islower() for char in text)

    if has_lowercase:
        print("The string contains lowercase letters.")
    else:
        print("The string does NOT contain lowercase letters.")

check_lowercase()