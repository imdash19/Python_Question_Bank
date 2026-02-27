# Write a Python program to find the digits that are missing from a given mobile number.

def find_missing_digits():
    mobile = input("Enter a mobile number: ")
    print('=' * 60)

    if not mobile.isdigit():
        print("Please enter a valid mobile number (digits only).")
        return

    all_digits = set('0123456789')
    present_digits = set(mobile)

    missing_digits = sorted(all_digits - present_digits)

    print("Digits present :", sorted(present_digits))
    print("Missing digits :", missing_digits)
    print("Total missing  :", len(missing_digits))

find_missing_digits()