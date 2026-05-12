# Write a program to filter numbers that are perfect squares.
# The program should accept a space-separated list of integers from the user.
# Each number must be checked to see if its square root is an integer.
# Python’s built-in filter() function must be used.
# The output should contain only perfect square numbers.

numbers = list(map(int, input("Enter space-separated integers: ").split()))

result = list(filter(lambda x: int(x ** 0.5) ** 2 == x, numbers))

print(result)
