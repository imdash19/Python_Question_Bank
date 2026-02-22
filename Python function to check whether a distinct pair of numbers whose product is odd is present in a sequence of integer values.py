# Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.

def check_odd_product_pair():
    lst = [int(val) for val in input(
        "Enter integers separated by space: "
    ).split()]

    print("=" * 60)
    odd_count = 0
    for num in lst:
        if num % 2 != 0:
            odd_count += 1

        if odd_count >= 2:
            print("A distinct pair whose product is odd is present.")
            return

    print("No such distinct pair exists.")

check_odd_product_pair()