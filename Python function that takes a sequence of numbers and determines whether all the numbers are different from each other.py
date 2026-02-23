# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def check_sequences():
    lst = [int(val) for val in input("Please enter your values separated with space: ").split()]
    print("=" * 60)

    if len(lst) == len(set(lst)):
        print("All numbers are different.")
    else:
        print("There are duplicate numbers in the sequence.")

check_sequences()