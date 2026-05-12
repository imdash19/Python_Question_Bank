# Write a program to filter numbers that are multiples of 7.
# The program should accept a space-separated list of integers from the user.
# Each number must be checked to see if it is divisible by 7 (n % 7 == 0).
# Python’s filter() function must be used.
# The output should contain only numbers divisible by 7.

numbers = list(map(int, input("Enter space-separated integers: ").split()))

result = list(filter(lambda n: n % 7 == 0, numbers))

print(result)
