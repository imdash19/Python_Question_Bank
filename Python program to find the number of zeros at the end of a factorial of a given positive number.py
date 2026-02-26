# Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
# Range of the number(n): (1 <= n <= 2*109).

n = int(input("Enter a positive number (1 <= n <= 2*10^9): "))

if n < 1:
    print("Please enter a valid positive number.")
else:
    count = 0
    divisor = 5

    while n // divisor > 0:
        count += n // divisor
        divisor *= 5

    print("Number of trailing zeros in", n, "factorial is:", count)