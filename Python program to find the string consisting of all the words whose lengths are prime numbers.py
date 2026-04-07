# Write a Python program to find the string consisting of all the words whose lengths are prime numbers.
# Input: The quick brown fox jumps over the lazy dog.
# Output: The quick brown fox jumps the
# Input: Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later.
# Output: Omicron Effect: Foreign Flights Won't On Dec 15,

def is_prime(s):
    n= len(s)
    if n > 2:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        return True

lst= [val for val in input('Please enter your string: ').split()]
for val in lst:
    if is_prime(val):
        print(val, end= ' ')