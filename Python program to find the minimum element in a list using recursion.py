# Write a program to find the minimum element in a list using recursion.
# The program should compare the first element with the minimum of the remaining list.
# Recursion continues until the list has only one element.
# The smallest value is returned as output.

def find_min(numbers):
    if len(numbers) == 1:
        return numbers[0]

    min_of_rest = find_min(numbers[1:])

    if numbers[0] < min_of_rest:
        return numbers[0]
    else:
        return min_of_rest

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = find_min(numbers)

print("Minimum element:", result)
