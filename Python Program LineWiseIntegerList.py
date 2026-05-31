# Reads multiple integers where each integer is provided on a separate line. The program collects these values into a list, useful for scenarios where input data comes line by line.

n = int(input())

numbers = []

for _ in range(n):
    numbers.append(int(input()))

print(numbers)
