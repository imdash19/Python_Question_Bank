#  Write a Python program to find common elements in a given list of lists.
# Original list: [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
# Common elements of the said list of lists: [2, 3]
# Original list: [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
# Common elements of the said list of lists: ['c']

def find_common_elements(lst):
    common = set(lst[0])
    for inner in lst[1:]:
        common = common.intersection(inner)

    return list(common)

try:
    lst= []
    n= int(input("Enter how many inner list you want: "))
    for i in range(n):
        print(f'Inside {i+1} inner list:')
        print('='*60)
        ilst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input().split()]
        print('='*60)
    lst.append(ilst)

except ValueError:
    print("Please enter a number...")

except Exception:
    print('Something went wrong! Please try again...')

else:
    print(f'''Original list: {lst}
Common elements of the said list of lists: {find_common_elements(lst)}''')