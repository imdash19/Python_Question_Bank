# Write a Python program to sort one list based on another list containing the desired indexes.
# Sample Output: ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
#     ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']

def sort_element_desired_index(lst, idx_lst):
    olst= []
    for i in idx_lst:
        olst.append(lst[i])
    return olst

try:
    lst= [val for val in input('Please enter your values separated with space: ').split()]
    print('='*60)

    idx_lst= [int(val) for val in input('Please enter your index values separated with space: ').split()]
    print('='*60)

except ValueError:
    print('Please enter numeric values...')

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst} \n {sort_element_desired_index(lst, idx_lst)}''')