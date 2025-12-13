#  Write a Python program to iterate a given list cyclically on specific index position.
# Original list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3: ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5: ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']

def iterate_list_cyclically(lst, idx):
    olst= lst[idx : ]
    olst+= lst[:idx]
    return olst

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
    print('='*60)
    idx= int(input('Please enter your index position: '))
    print('='*60)

except ValueError:
    print('Please enter an integer')

except Exception:
    print('Something went wrong! Please try again...')

else:
    print(f'''Original list: {lst}
 Iterate the said list cyclically on specific index position {idx}: {iterate_list_cyclically(lst, idx)}''')