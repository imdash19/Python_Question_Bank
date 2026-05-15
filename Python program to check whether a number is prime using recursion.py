# Write a program to check whether a number is prime using recursion.
# The program should divide the number by increasing values starting from 2.
# If any divisor divides the number completely, it is not prime.
# The recursion stops when divisor exceeds square root of the number.
# Output should be True or False.

def is_prime(number, divisor=2):
    if number < 2:
        return False

    if divisor * divisor > number:
        return True

    if number % divisor == 0:
        return False

    return is_prime(number, divisor + 1)

number = int(input("Enter a number: "))

print(is_prime(number))
