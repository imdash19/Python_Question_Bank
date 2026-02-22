# Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number.

def sum_of_cube():
    n = int(input("Please enter your number: "))
    print("=" * 60)

    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    total = 0
    for i in range(1, n):
        total += i ** 3

    print(f"Sum of cubes of all positive integers less than {n} is: {total}")

sum_of_cube()