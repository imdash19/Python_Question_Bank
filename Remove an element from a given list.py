# Write a Python program to remove an element from a given list.
# Original list: ['Guido Van Rossum', 98, 'Math', 90, 'Science']
# After deleting an element, using index of the element: [98, 'Math', 90, 'Science']

def remove_element(lst, idx):
    if idx < 0 or idx >= len(lst):
        return 'Index out of range'
    lst.pop(idx)
    return lst

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your value separated with space: ').split()]
    print('='*60)

    idx= int(input('Please enter the index of the element to be removed: '))
    print('='*60)

except ValueError:
    print('Please enter a numeric value...')

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst}
After deleting an element, using index of the element: {remove_element(lst, idx)}''')