# Write a Python program to create a list with the non-unique values filtered out.
# Sample Output: [1, 3, 5]

def find_nonunique_values(lst):
    olst= []
    for val in lst:
        if lst.count(val) == 1:
            olst.append(val)
    return olst

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
    print('='*60)

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst} \n Output: {find_nonunique_values(lst)}''')