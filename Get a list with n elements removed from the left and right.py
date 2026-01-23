# 	Write a Python program to get a list with n elements removed from the left, right.
# Original list elements: [1, 2, 3]
# Remove 1 element from left of the said list: [2, 3]
# Remove 1 element from right of the said list: [1, 2]
# Original list elements: [1, 2, 3, 4]
# Remove 2 elements from left of the said list: [3, 4]
# Remove 2 elements from right of the said list: [1, 2]
# Original list elements: [1, 2, 3, 4, 5, 6]
# Remove 7 elements from left of the said list: [2, 3, 4, 5, 6]
# Remove 7 elements from right of the said list: [1, 2, 3, 4, 5]

def remove_from_left(n, lst):
    if n >= len(lst):
        return lst[1:]
    return lst[n:]

def remove_from_right(n, lst):
    if n >= len(lst):
        return lst[:-1]
    return lst[:-n]


lst = [int(val) if val.lstrip('-').isdigit() else val for val in input('Please enter your values separated with space: ').split()]
print('=' * 60)

n = int(input('Please enter how many values you want to remove: '))
print('=' * 60)

print(f'''Original list elements: {lst}
Remove {n} elements from left of the said list: {remove_from_left(n, lst)}
Remove {n} elements from right of the said list: {remove_from_right(n, lst)}''')