# Write a program to filter numbers that have an odd number of digits.
# The program should accept a space-separated list of integers from the user.
# Each number must be evaluated to count its digits.
# Python’s filter() function must be used.
# The output should contain only numbers with an odd number of digits.

nums = list(map(int, input("Enter space-separated numbers: ").split()))

result = list(filter(lambda x: len(str(abs(x))) % 2 != 0, nums))

print(result)
