# Write a Python program to find the total number of even or odd divisors of a given integer.

def even_odd_divisors():
    n = int(input("Enter a positive integer: "))
    print('=' * 60)

    if n <= 0:
        print("Please enter a positive integer.")
        return

    print("""
    1. Even divisors
    2. Odd divisors
    """)

    ch = int(input("Enter your choice (1 / 2): "))
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            if ch == 1 and i % 2 == 0:
                divisors.append(i)
            elif ch == 2 and i % 2 != 0:
                divisors.append(i)

    if ch not in [1, 2]:
        print("Please enter a valid choice.")
        return

    print('=' * 60)
    print("Divisors:", divisors)
    print("Total count:", len(divisors))

even_odd_divisors()