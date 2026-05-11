# Write a program to validate phone numbers.
# The program should accept a space-separated list of numbers as strings.
# Each number must be checked for length and digits.
# A valid phone number must contain exactly 10 digits.
# Python’s map() function should be used for validation.
# The output should be a list of boolean values.

def is_valid(number):
    return len(number) == 10 and number.isdigit()

if __name__ == "__main__":
    numbers = input().split()

    result = list(map(is_valid, numbers))

    print(result)
