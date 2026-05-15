# Write a program to find the maximum element in a list using recursion. 
# The program should compare the first element with the maximum of the remaining list.
# Recursion continues until only one element is left. 
# The result should be the largest value in the list.

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]

    max_of_rest = find_max(numbers[1:])

    if numbers[0] > max_of_rest:
        return numbers[0]
    else:
        return max_of_rest

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = find_max(numbers)

print("Maximum element:", result)
