# Reads integers from input until a specific sentinel value (commonly -1) is encountered. The program collects all preceding integers into a list, excluding the sentinel itself.

numbers = []

while True:
    num = int(input())

    if num == -1:
        break

    numbers.append(num)

print(numbers)
