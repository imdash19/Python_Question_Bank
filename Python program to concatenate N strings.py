# Write a Python program to concatenate N strings.

def concatenate_n_strings():
    n = int(input("Please enter how many strings you want to enter: "))

    if n <= 0:
        print("Please enter a positive integer")
        return

    strings = input("Please enter your strings separated by space: ").split()

    if len(strings) != n:
        print("Number of strings entered does not match the expected count.")
    else:
        result = ""
        for s in strings:
            result += s
        print("Concatenated string:", result)

concatenate_n_strings()