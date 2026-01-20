# 	Write a Python program to perform a deep flattens a list.
# Sample Output:
# Original list elements: [1, [2], [[3], [4], 5], 6]
# Deep flatten the said list: [1, 2, 3, 4, 5, 6]
# Original list elements: [[[1, 2, 3], [4, 5]], 6]
# Deep flatten the said list: [1, 2, 3, 4, 5, 6]

def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

original_list = eval(input("Enter a list (can be nested): "))
flattened_list = deep_flatten(original_list)

print("Original list elements:", original_list)
print("Deep flatten the said list:", flattened_list)