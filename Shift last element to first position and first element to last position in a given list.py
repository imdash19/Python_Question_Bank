#  Write a Python program to shift last element to first position and first element to last position in a given list.
# Original list: [1, 2, 3, 4, 5, 6, 7]
# Shift last element to first position and first element to last position of the said list: [7, 2, 3, 4, 5, 6, 1]
# Original list: ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
# Shift last element to first position and first element to last position of the said list: ['f', 'd', 'f', 'd', 's', 's', 'd', 's']

def shift_first_and_last_element_position(lst):
    olst= lst[1:-1]
    fe= lst[0]
    le= lst[-1]
    olst.insert(0,le)
    olst.append(fe)
    return olst

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
    print('='*60)

except Exception:
    print('Something went wrong:( Please try again...')

else:
    print(f'''Original list: {lst}
 Shift last element to first position and first element to last position of the said list: {shift_first_and_last_element_position(lst)}''')