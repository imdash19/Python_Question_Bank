# Write a Python program to print the number of prime numbers that are less than or equal to a given number.
# Input:
# n (1 <= n <= 999,999)
# Input the number(n): 35
# Number of prime numbers which are less than or equal to n.: 11

def get_prime_inrange():
    n = int(input("Input the number(n): "))
    count = 0

    if 1 <= n <= 999999:
        for i in range(2, n + 1):
            prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                count += 1
        print("Number of prime numbers which are less than or equal to n.:", count)
    else:
        print("Invalid input")

get_prime_inrange()