#  Write a Python program to compare two given lists and find the indices of the values present in both lists.
# Original lists: [1, 2, 3, 4, 5, 6]
# [7, 8, 5, 2, 10, 12]
# Compare said two lists and get the indices of the values present in both lists: [1, 4]
# Original lists: [1, 2, 3, 4, 5, 6]
# [7, 8, 5, 7, 10, 12]
# Compare said two lists and get the indices of the values present in both lists: [4]
# Original lists: [1, 2, 3, 4, 15, 6]
# [7, 8, 5, 7, 10, 12]
# Compare said two lists and get the indices of the values present in both lists: []

def get_index_common_elements(lst1, lst2):
    olst= []
    for val in lst1:
        if val in lst2:
            l1= lst1.index(val)
            l2= lst2.index(val)
            olst.append(l1)
            olst.append(l2)
    return olst

try:
    lst1= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your list elements separated with space: ').split()]
    print('='*60)

    lst2= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your list elements separated with space: ').split()]
    print('=' * 60)

except Exception:
    print('Something went wrong:( Please try again later...')

else:
    print(f'''Original lists: {lst1} \n {lst2}
 Compare said two lists and get the indices of the values present in both lists: {get_index_common_elements(lst1, lst2)}''')