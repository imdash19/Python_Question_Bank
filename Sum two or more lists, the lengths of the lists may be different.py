#  Write a Python program to sum two or more lists, the lengths of the lists may be different.
# Original list: [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths: [4, 8, 8]
# Original list: [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths: [8, 6, 4]

def sum_list_elements(lst):
    olst= []
    max_len = 0
    for ilst in lst:
        if len(ilst) > max_len:
            max_len = len(ilst)

    for i in range(max_len):
        s = 0
        for ilst in lst:
            if i < len(ilst):
                s += ilst[i]
        olst.append(s)
    return olst

try:
    lst= []
    n= int(input('Please enter how many inner list you want: '))
    if n <= 0:
        print('Please enter a positive integer')
    for i in range(n):
        print('='*60)
        print(f'Inside {i+1} inner list')
        print('=' * 60)
        ilst= [int(val) for val in input('Please enter your list elements separated with space: ').split()]
        lst.append(ilst)

except ValueError:
    print('Please enter an integer...')

except Exception:
    print('Something went wrong:( Please try again...')

else:
    print(f'''Original list: {lst}
 Sum said lists with different lengths: {sum_list_elements(lst)}''')