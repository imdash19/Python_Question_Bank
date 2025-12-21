# Write a Python program to create a list with the unique values filtered out.
# Sample Output: [2, 4]

def list_unique_values(lst):
    olst = []
    for val in lst:
        if lst.count(val) > 1:
            if val not in olst:
                olst.append(val)
    return olst

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
    print('='*60)

except:
    print('Something went wromg :( Please try again later...')

else:
    print(f'''Original list: {lst} \n Output: {list_unique_values(lst)}''')