# Write a program to filter numbers divisible by 5 from a list.
# The program should accept a space-separated list of integers from the user.
# Each number should be tested using modulus 5 (% 5).
# Python’s filter() function must be used.
# The output should be a list of numbers divisible by 5.

numbers = list(map(int, input("Enter space-separated integers: ").split()))

result = list(filter(lambda x: x % 5 == 0, numbers))

print(result)
