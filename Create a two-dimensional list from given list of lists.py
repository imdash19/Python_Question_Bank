# 	Write a Python program to create a two-dimensional list from given list of lists.
# Sample Output: [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
#     [(1, 4), (2, 5)]

def create_2d_list(lst):
    return [tuple(x) for x in zip(*lst)]


lst = []
n = int(input('Please enter number of inner lists: '))
print('=' * 60)

for i in range(n):
    values = [int(val) for val in input(
        f'Please enter values for list {i+1} separated with space: '
    ).split()]
    lst.append(values)

print('=' * 60)

print(f'''Original list: {lst}
Two dimensional list: {create_2d_list(lst)}''')