# Write a Python program which accepts an even number (>=4, Goldbach number) from the user and creates combinations which express the given number as a sum of two prime numbers. Print the number of combinations.
# Goldbach number: A Goldbach number is a positive even integer that can be expressed as the sum of two odd primes.[4] Since four is the only even number greater than two that requires the even prime 2 in order to be written as the sum of two primes, another form of the statement of Goldbach's conjecture is that all even integers greater than 4 are Goldbach numbers.
# The expression of a given even number as a sum of two primes is called a Goldbach partition of that number. The following are examples of Goldbach partitions for some even numbers:
# 6 = 3 + 3
# 8 = 3 + 5
# 10 = 3 + 7 = 5 + 5
# 12 = 7 + 5
# ...
# 100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
# Input an even number (0 to exit):
# 100
# Number of combinations:
# 6

while True:
    n = int(input("Input an even number (0 to exit):\n"))
    if n == 0:
        break
    count = 0
    a = 3
    while a <= n // 2:
        p = True
        i = 2
        while i * i <= a:
            if a % i == 0:
                p = False
                break
            i += 1
        if p:
            b = n - a
            q = True
            j = 2
            while j * j <= b:
                if b % j == 0:
                    q = False
                    break
                j += 1
            if q:
                count += 1
        a += 2
    print("Number of combinations:")
    print(count)