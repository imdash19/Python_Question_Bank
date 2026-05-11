# Write a program to check whether each number in a list is prime. 
# The program should accept a space-separated list of integers from the user.
# It should evaluate each number individually. 
# A helper function must be used to verify primality. 
# The map() function should apply this check to all elements.
# The output should be a list of boolean values.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    numbers = list(map(int, input().split()))

    result = list(map(is_prime, numbers))

    print(result)
