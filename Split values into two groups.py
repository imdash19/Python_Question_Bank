# Write a Python program to split values into two groups, based on the result of the given filtering function.
# Sample Output: [['white'], ['red', 'green', 'black']]

def split_values_into_two_groups(lst):
    olst= []
    lst1= []
    lst2= []
    for i in range(len(lst)):
        if len(lst[i]) > 4:
            lst1.append(lst[i])
        else:
            lst2.append(lst[i])
    olst.append(lst1)
    olst.append(lst2)
    return olst

try:
    lst= [val for val in input('Please enter your values separated with space: ').split()]
    print('='*60)

except:
    print('Something went wrong :( Try again later...')

else:
    print(f'''Original list: {lst}
Sample Output: {split_values_into_two_groups(lst)}''')