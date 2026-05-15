# Write a program to check whether a list is sorted using recursion. 
# The program should compare consecutive elements. 
# If all elements follow ascending order, return True.
# Otherwise return False. Recursion ends when list size becomes 1.

def is_sorted(numbers):
    if len(numbers) == 1:
        return True

    if numbers[0] > numbers[1]:
        return False

    return is_sorted(numbers[1:])

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = is_sorted(numbers)

print(result)
