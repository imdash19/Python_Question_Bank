# Write a Python program to test whether all numbers in a list are greater than a certain number.

def check_greater_than():
    lst = [int(val) for val in input(
        "Please enter your numbers separated with space: "
    ).split()]

    print("=" * 60)

    n = int(input("Please enter your number to check greater than: "))
    print("=" * 60)

    result = True

    for val in lst:
        if val <= n:
            result = False
            break

    if result:
        print(f"All numbers in the list {lst} are greater than {n}")
    else:
        print(f"All numbers in the list {lst} are not greater than {n}")

check_greater_than()