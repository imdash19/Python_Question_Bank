# Write a Python program to remove all the values except integer values from a given array of mixed values.
# Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
# After removing all the values except integer values from the said array of mixed values: [12, 0]

def get_integer_from_mixed_array(lst):
    olst= []
    for val in lst:
        if type(val) == int:
            olst.append(val)
    return olst

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else float(val) if (val.lstrip('-')).isdecimal() else val for val in input('Please enter your values separated with space: ').split()]
    print('='*60)

except:
    print('Please enter integer values only...')

else:
    print(f'''Original list: {lst}
 After removing all the values except integer values from the said array of mixed values: {get_integer_from_mixed_array(lst)}''')