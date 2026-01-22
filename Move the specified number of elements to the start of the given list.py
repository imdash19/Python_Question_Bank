# 	Write a Python program to move the specified number of elements to the start of the given list.
# Sample Output: [4, 5, 6, 7, 8, 1, 2, 3]
#     [6, 7, 8, 1, 2, 3, 4, 5]
#     [1, 2, 3, 4, 5, 6, 7, 8]
#     [1, 2, 3, 4, 5, 6, 7, 8]
#     [8, 1, 2, 3, 4, 5, 6, 7]
#     [2, 3, 4, 5, 6, 7, 8, 1]

def move_to_first(lst, n):
    return lst[-n:] + lst[:-n]

lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
print('='*60)

n= int(input('Please enter how many elements you want to move to first: '))
print('='*60)

print(f'''Original list: {lst}
List after moving {n} elements to first {move_to_first(lst, n)}''')