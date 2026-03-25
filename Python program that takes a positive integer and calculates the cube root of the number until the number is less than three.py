# Write a Python program that takes a positive integer and calculates the cube root of the number until the number is less than three. Count the number of steps to complete the task.
# Sample Data:
# (3) -> 1
# (39) -> 2
# (10000) -> 2

def count_steps():
    n = int(input())

    if n <= 0:
        return 0

    count = 0

    while n >= 3:
        n = n ** (1 / 3)
        count += 1

    return count


print(count_steps())