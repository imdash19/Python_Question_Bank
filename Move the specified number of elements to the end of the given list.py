# 	Write a Python program to move the specified number of elements to the end of the given list.
# Sample Output: [4, 5, 6, 7, 8, 1, 2, 3]
#     [6, 7, 8, 1, 2, 3, 4, 5]
#     [1, 2, 3, 4, 5, 6, 7, 8]
#     [1, 2, 3, 4, 5, 6, 7, 8]
#     [8, 1, 2, 3, 4, 5, 6, 7]
#     [2, 3, 4, 5, 6, 7, 8, 1]

def move_elements_to_end(lst, n):
    slst= []
    slst= lst[n:] + lst[:n]
    return slst

lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
print('='*60)

n= int(input('Please enter the number of elements you want to move to end: '))
print('='*60)

print(f'''Original list: {lst}
After moving {n} elements to the end of the list: {move_elements_to_end(lst, n)}''')