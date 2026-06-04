# Reads an integer and checks whether it is a prime number. The program validates primality using mathematical algorithms and provides appropriate output.

n = int(input())

if n < 2:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")