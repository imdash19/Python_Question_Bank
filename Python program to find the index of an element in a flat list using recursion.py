# Write a program to find the index of an element in a flat list using recursion.
# User enters list and target element.
# Each recursive call checks first element: returns 0 if found;
# else 1 + call on remaining list.
# If not found, return -1.

def find_index(nums, target):
    if len(nums) == 0:
        return -1
    
    if nums[0] == target:
        return 0
    
    result = find_index(nums[1:], target)
    
    if result == -1:
        return -1
    else:
        return 1 + result

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter target element: "))

print(find_index(numbers, target))
