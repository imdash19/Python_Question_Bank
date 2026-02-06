# Write a Python program to calculate sum of digits of a number.

def sum_of_digits():
    num = int(input("Enter your number: "))
    original_num = num
    snum = 0

    while num > 0:
        snum += num % 10
        num //= 10

    print(f"Sum of digits of {original_num} is {snum}")

sum_of_digits()