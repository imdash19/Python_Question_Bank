# Write a Python program to compute the sum of non-zero groups (separated by zeros) of a given list of numbers.
# Original list: [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
# Compute the sum of non-zero groups (separated by zeros) of the said list of numbers: [15, 38, 15, 27]

def sum_nonzero_groupsof_in_list(lst):
    olst= []
    ilst= []
    for val in lst:
        if val != 0:
            ilst.append(val)
        else:
            if sum(ilst) != 0:
                olst.append(sum(ilst))
            ilst= []
    return olst

try:
    lst= [int(val) for val in input('Please enter your list numbers separated by space: ').split()]
    print('='*60)

except ValueError:
    print('Please enter numbers only...')

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst}
Compute the sum of non-zero groups (separated by zeros) of the said list of numbers: {sum_nonzero_groupsof_in_list(lst)}''')