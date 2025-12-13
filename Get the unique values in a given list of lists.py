#  Write a Python program to get the unique values in a given list of lists.
# Original list: [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# Unique values of the said list of lists: [0, 1, 2, 3, 4, 5, 7]
# Original list: [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
# Unique values of the said list of lists: ['e', 'd', 'c', 'b', 'x', 'k', 'n', 'h', 'g', 'j', 'i', 'a', 'l', 'y', 'v', 'z']

def get_unique_value(lst):
    olst= []
    for val in lst:
        for vl in val:
            if vl not in olst:
                olst.append(vl)
    return olst

try:
    lst= []
    n= int(input('Please enter how many inner list you want: '))
    for i in range(n):
        print(f'Inside {i+1} inner list: ')
        print('='*60)
        ilst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
        print('='*60)
        lst.append(ilst)

except ValueError:
    print('Please enter numbers only...')

except:
    print('Something went wrong :( Please try again...')

else:
    print(f'''Original list: {lst}
 Unique values of the said list of lists: {get_unique_value(lst)}''')